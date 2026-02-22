from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from .models import Post, Like

User = get_user_model()


class LikeTestCase(APITestCase):

    def setUp(self):
        self.user1 = User.objects.create_user(username='user1', password='pass123')
        self.user2 = User.objects.create_user(username='user2', password='pass123')

        self.post = Post.objects.create(
            author=self.user1,
            content="Test Post"
        )

    def test_like_post(self):
        self.client.login(username='user2', password='pass123')

        response = self.client.post(
            reverse('like-post', args=[self.post.id])
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(Like.objects.count(), 1)

    def test_prevent_duplicate_like(self):
        self.client.login(username='user2', password='pass123')
        self.client.post(reverse('like-post', args=[self.post.id]))
        response = self.client.post(reverse('like-post', args=[self.post.id]))

        self.assertEqual(response.status_code, 400)

    def test_unlike_post(self):
        self.client.login(username='user2', password='pass123')
        self.client.post(reverse('like-post', args=[self.post.id]))

        response = self.client.post(
            reverse('unlike-post', args=[self.post.id])
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Like.objects.count(), 0)