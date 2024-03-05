from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site

from service.models import Letter


def mailCreator(request, title, txt):
    user = Letter.objects.all()
    from_email = settings.EMAIL_HOST_USER
    current_site = get_current_site(request)
    for email in user:
        mail_subject = title 
        txt = txt 
        message = render_to_string(template_name="last_news.html", context={
            "domain": current_site,
            "txt": txt,
        })
        mail = EmailMessage(mail_subject, message, from_email, to=email)
