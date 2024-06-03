from django.test import TestCase

from .models import User 


class LogInTest(TestCase):
    def setUp(self):
        self.credentials = {
            'phone': '09026386221',
            'password': '123'}
        User.objects.create(**self.credentials)
    
    def test_login(self):
        response = self.client.post('/user/', self.credentials, follow=True)
        self.assertTrue(response.context['user'])
