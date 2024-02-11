from django.utils import timezone
from django.core.exceptions import ValidationError


def passedDays(date):
    if date < timezone.now().date():
        raise ValidationError("شما نمیتوانید از روز های گذشته انتخاب کنید")
    else:
        return date


def noFriday(date):
    if date.weekday() == 4:
        raise ValidationError("این روز تعطیل میباشد")
    else:
        return date
