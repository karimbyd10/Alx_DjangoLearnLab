from rest_framework import generics, permissions
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from .serializers import UserRegisterSerializer, UserProfileSerializer
from .models import CustomUser
from rest_framework import viewsets, status
from rest_framework.decorators import action

# Registration
class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserRegisterSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = CustomUser.objects.get(username=response.data['username'])
        token, created = Token.objects.get_or_create(user=user)
        response.data['token'] = token.key
        return response

# Login
class LoginView(APIView):
    permission_classes = []

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        return Response({'error': 'Invalid credentials'}, status=400)

# User Profile
class UserProfileView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=["post"])
    def follow(self, request, pk=None):
        user_to_follow = self.get_object()

        if request.user == user_to_follow:
            return Response(
                {"detail": "You cannot follow yourself."},
                status=status.HTTP_400_BAD_REQUEST
            )

        request.user.following.add(user_to_follow)

        return Response({"detail": "Successfully followed user."})

    @action(detail=True, methods=["post"])
    def unfollow(self, request, pk=None):
        user_to_unfollow = self.get_object()

        request.user.following.remove(user_to_unfollow)

        return Response({"detail": "Successfully unfollowed user."})
    
class FollowUserView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        try:
            user_to_follow = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response(
                {"detail": "User not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        if request.user == user_to_follow:
            return Response(
                {"detail": "You cannot follow yourself."},
                status=status.HTTP_400_BAD_REQUEST
            )

        request.user.following.add(user_to_follow)

        return Response(
            {"detail": "Successfully followed user."},
            status=status.HTTP_200_OK
        )


class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        try:
            user_to_unfollow = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response(
                {"detail": "User not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        request.user.following.remove(user_to_unfollow)

        return Response(
            {"detail": "Successfully unfollowed user."},
            status=status.HTTP_200_OK
        )
    