from django.test import TestCase
from blog.models import Post
from django.contrib.auth.models import User


class PostModelTests(TestCase):

    def setUp(self):
        user = User.objects.create(username="Dennis123")
        Post.objects.create(
        author=user, title="Sample Title", text="Sample Text")
