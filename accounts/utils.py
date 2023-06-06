from django.core.mail import send_mail
from django.conf import settings




def sendSimpleEmail(title,name:str, msg :str, contact:str, reciever):
    subject = title
    message = f"Yuboruvchi : {name.title()}\nAloqa : {contact}\n\nXabar matni : \n{msg}"
    email_from = settings.EMAIL_HOST_USER
    recipient = [reciever]
    ms = send_mail( subject, message, email_from, recipient)
    print("Sent Message", ms)
    return True

