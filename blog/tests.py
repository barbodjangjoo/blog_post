from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Post

class PostTest(TestCase):
    def setUp(self):
        CustomUser = get_user_model()
        self.user = CustomUser.objects.create_user(username='user1')
        self.post1= Post.objects.create(
            title= 'Post1',
            text= 'This is description',
            status= True,
            author= self.user,
        )

    def test_post_list_view_url_by_name(self):
        response = self.client.get(reverse('blog:post_list'))
        self.assertEqual(response.status_code, 200)

    def test_post_list_by_url(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_post_title_on_home(self):
        response = self.client.get(reverse('blog:post_list'))
        self.assertContains(response, 'Post1')

    def test_post_detail_url(self):
        response = self.client.get('//1')
        self.assertEqual(response.status_code, 200)

    def test_post_detail_view_url_by_name(self):
        response = self.client.get(reverse('blog:post_detail', args=[self.post1.id]))
        self.assertEqual(response.status_code, 200)

    def test_post_details_on_blog_detail_pages(self):
        response = self.client.get('//1')
        self.assertContains(response, self.post1.title)
        self.assertContains(response, self.post1.text)

    def test_status_404_if_post_id_not_exist(self):
        response = self.client.get(reverse('blog:post_detail', args=[999]))
        self.assertEqual(response.status_code, 404)