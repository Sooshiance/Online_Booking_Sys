from django.test import TestCase

from .models import ArrotModel

from user.models import User


class ArrotTest(TestCase):
    """"""

    def setUp(self) -> None:
        self.user = User.objects.create(phone="09123456789", email="myuser@gmail.com", username="myuser", first_name="ali", last_name="reza")
        self.arrot = ArrotModel.objects.create(user=self.user, title='هایفو تراپی',hour='08-10',date="1403-11-21",jtime="1403-11-21")
        return super().setUp()
    

    def test_addingTurn(self):
        arr = ArrotModel.objects.create(user=self.user,title='میکرونیدلینگ',hour='08-10',date="1403-10-21",jtime="1403-10-21")
        self.assertEqual(ArrotModel.objects.all().count(), 2)
    

    def test_checkUser(self):
        a = ArrotModel.objects.create(user=self.user,title='هایفو تراپی',hour='12-14',date="1403-11-21",jtime="1403-11-21")
        self.assertEqual(a.user, self.user)
