from django.test import TestCase
from user.models import User

from question.models import Question, RepetitiveQuestion


class TestQuestion(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(phone="09123456789", email="myuser@gmail.com", username="myuser", first_name="ali", last_name="reza")
        self.ask = Question.objects.create(title="مشکل پوستی", txt="آیا با داشتن مشکل پوستی میتوان از خدمات استفاده کرد", user=self.user)
        return super().setUp()
    
    def test_questionCount(self):
        c = Question.objects.all()
        self.assertEqual(c.count(), 1)


class TestQuestion(TestCase):
    def setUp(self) -> None:
        self.ask = RepetitiveQuestion.objects.create(title="مشکل پوستی", txt="آیا با داشتن مشکل پوستی میتوان از خدمات استفاده کرد")
        return super().setUp()
    
    def test_questionCount(self):
        c = Question.objects.all()
        self.assertEqual(c.count(), 1)
