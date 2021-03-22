from django.core.mail import EmailMultiAlternatives


def send_mail(subject='', body='', from_email=None, to=None, bcc=None,
              connection=None, attachments=None, headers=None, alternatives=None,
              cc=None, reply_to=None, attach_alternative_content=None, attach_alternative_mimetype=None):
    """
    Send a django.core.mail.EmailMultiAlternatives to `to`.
    """
    # Email subject must not contain newlines.
    subject = ''.join(subject.splitlines())
    email_message = EmailMultiAlternatives(
        subject, body, from_email, to, bcc, connection, attachments, headers, alternatives, cc, reply_to
    )
    if attach_alternative_content is not None and attach_alternative_mimetype is not None:
        email_message.attach_alternative(attach_alternative_content, attach_alternative_mimetype)
    email_message.send()
