from django.core.mail import EmailMessage
from djoser.signals import user_registered


def send_welcome_email(sender, user, request):
    email = EmailMessage(
        'Welcome to KLang',
        f"Welcome {user.username} to KLang, this just confirms your registration!",
        'klang@ketzu.net'
        [user.email],
        [],
        reply_to=["klang@ketzu.net"]
    )
    email.send(fail_silently=True)


#user_registered.connect(send_welcome_email)
