from django.test import TestCase
from blog.models import Post
from django.contrib.auth.models import User


class PostModelTests(TestCase):

    def setUp(self):
        user = User.objects.create(username="Dennis123")
        Post.objects.create(
            author=user,
            title="Sample Title",
            text="Sample Text")

    def test_post_title(self):
        post = Post.objects.get(title="Sample Title")
        self.assertEquals(f'{post.title}', "Sample Title")

    def test_post_content(self):
        post = Post.objects.get(title="Sample Title")
        self.assertEquals(f"{post.text}", "Sample Text")

    def test_post_string_representation(self):
        post = Post.objects.get(title="Sample Title")
        self.assertEquals(str(post), f"{post.title}")
