from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.reverse import reverse as api_reverse
from django.contrib.auth import get_user_model
from apiapp.models import BlogPost
#automated
#new /blank db

User = get_user_model()

class BlogPostAPITestCase(APITestCase):
	def setUp(self):
		user_obj = User(username='kimbali', email='eric@niyo.com')
		user_obj.set_password('kigali123')
		user_obj.save()

		blog_post=BlogPost.objects.create(

			user=user_obj,
			title='My test tile 1',
			content='test content 1'
			)


	def test_single_user(self):
		user_count= User.objects.count()
		self.assertEqual(user_count, 1)

	def test_single_post(self):
		post_count= BlogPost.objects.count()
		self.assertEqual(post_count, 1)

	def test_get_list(self):
		#tested get list item
		data={}
		url=api_reverse('api-posting:api-listcreate')
		response=self.client.get(url, data, formt='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		# print(response.data)

	# def test_post_item(self):
	# 	#tested get list item
	# 	data={"title":"I have become same  one else", 'content':'become somethink else'}
	# 	url=api_reverse('api-posting:api-listcreate')
	# 	response=self.client.post(url, data, formt='json')
	# 	self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
	def test_user_login(self):
		data={
			'username':'kimbali',
			'password':'kigali123'
		}
		url = api_reverse("api-login")
		response = self.client.post(url, data)
		print(response.data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)


