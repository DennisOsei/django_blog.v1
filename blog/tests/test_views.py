from django.test import TestCase
from blog import views
from blog.models import Post
from django.contrib.auth.models import User
from django.urls import reverse

class HomePageTests(TestCase):

    def setUp(self):
        user = User.objects.create(username="Dennis123")
        Post.objects.create(
            author=user,
            title="Sample Title",
            text="Sample Text",
            )

    def test_home_page_status_code(self):
        response = self.client.get("/")
        self.assertEquals(response.status_code, 200)

    def test_view_url_acessible_by_name(self):
        response = self.client.get(reverse("post_list"))
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse("post_list"))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/post_list.html")



        

   

        
