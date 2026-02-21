from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import (
    CommentDeleteView,
    CommentUpdateView,
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)
from .views import PostSearchView, PostByTagListView

urlpatterns += [
    path('', views.post_list, name='post_list'),

    path('register/', views.register, name='register'),

    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),

    path('logout/', auth_views.LogoutView.as_view( template_name='blog/logout.html'), name='logout'),

    path('profile/', views.profile, name='profile'),

    path('posts/', PostListView.as_view(), name='post_list'),

    path('post/new/', PostCreateView.as_view(), name='post_create'),

    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),

    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),

    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),

]
urlpatterns += [
    path('post/<int:pk>/comments/new/',
         CommentCreateView.as_view(),
         name='comment_create'),

    path('comment/<int:pk>/update/',
         CommentUpdateView.as_view(),
         name='comment_update'),

    path('comment/<int:pk>/delete/',
         CommentDeleteView.as_view(),
         name='comment_delete'),
]

urlpatterns += [
    path('search/', PostSearchView.as_view(), name='post_search'),
    path('tags/<str:tag_name>/', PostByTagListView.as_view(), name='posts_by_tag'),
    path(
        'tags/<slug:tag_slug>/',
        PostByTagListView.as_view(),
        name='posts_by_tag'
    ),

]