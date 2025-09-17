from django.core.mail import EmailMessage
import os

class Util:
  @staticmethod
  def send_email(data):
    print('send_email',data)
    print('os.environ.get()',os.environ.get('EMAIL_FROM'))
    
    email = EmailMessage(
      subject=data['subject'],
      body=data['body'],
      from_email=os.environ.get('EMAIL_FROM'),
      to=[data['to_email']]
    )
    email.send()