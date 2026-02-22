from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination

from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Post, Like
from notifications.utils import create_notification


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 50


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    pagination_class = StandardResultsSetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        following_users = self.request.user.following.all()
        return Post.objects.filter(author__in=following_users).order_by('-created_at')

@api_view(['POST'])
@permission_classes([IsAuthenticated])
    def like_post(request, pk):
      post = get_object_or_404(Post, pk=pk)

      like, created = Like.objects.get_or_create(
        user=request.user,
        post=post
    )

    if not created:
        return Response(
            {"detail": "You already liked this post."},
            status=status.HTTP_400_BAD_REQUEST
        )

    create_notification(
        actor=request.user,
        recipient=post.author,
        verb="liked your post",
        target=post
    )

        return Response(
        {"detail": "Post liked successfully."},
        status=status.HTTP_201_CREATED
    )


@api_view(['POST'])
@permission_classes([IsAuthenticated])
    def unlike_post(request, pk):
      post = get_object_or_404(Post, pk=pk)

      like = Like.objects.filter(
        user=request.user,
        post=post
    ).first()

    if not like:
        return Response(
            {"detail": "You have not liked this post."},
            status=status.HTTP_400_BAD_REQUEST
        )

    like.delete()

    return Response(
        {"detail": "Post unliked successfully."},
        status=status.HTTP_200_OK
    )