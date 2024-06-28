from django.shortcuts import render
from django.core.mail import EmailMessage
from django.http import HttpResponse
from .models import EmailLog
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
import uuid


def send_email_with_tracking(request):
    email_id = str(uuid.uuid4())

    mail_subject = "Reset your password"

    message = render_to_string("email.html", {"email_id": email_id})
    email = EmailMessage(mail_subject, message, 'from@example.com', ['deepakpvt26@gmail.com'])
    email.content_subtype = 'html'
    email.send()

    EmailLog.objects.create(email_id=email_id, opened=False)
    return HttpResponse({"message":"Success"})


def email_opened(request, email_id):
    email_log, created = EmailLog.objects.get_or_create(email_id=email_id)
    email_log.opened = True
    print("worked.............................")
    email_log.save()

    pixel = b"\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x21\xF9\x04\x01\x00\x00\x00\x00\x2C\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02\x4C\x01\x00\x3B"
    return HttpResponse(pixel, content_type="image/gif")


def try1(request):
    return render(request, "email.html")

def check(request):
    return HttpResponse({"message11":"Running.."})
