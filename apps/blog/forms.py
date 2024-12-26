import logging
import os

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from django import forms
from django.conf import settings
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

logger = logging.getLogger("django")


def sendgrid_mail(from_email, to_emails, subject, html_content):
    message = Mail(
        from_email=from_email,
        to_emails=to_emails,
        subject=subject,
        html_content=html_content
    )
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        logging.info("Sendgrid response status: %s", response.status_code)
        logging.info("SendGrid response body: %s", response.body)
        logging.info("SendGrid response headers: %s", response.headers)
    except Exception:
        logging.exception("email was NOT sent")


class ContactForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields["captcha"].label = False

    sender = forms.CharField(max_length=256)
    email = forms.EmailField(max_length=256)
    subject = forms.CharField(max_length=256)
    message = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(attrs=dict(cols=19, rows=10, placeholder="2000 character limit")),
    )
    # captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)

    helper = FormHelper()
    helper.add_input(Submit("submit", "Send Email"))
    helper.layout = Layout(
        Field("sender"),
        Field("email"),
        Field("subject"),
        Field("message"),
        # Field('captcha', style="border: none; padding: 0px"),
    )

    def mail(self):
        logging.info("sending email via SendGrid")
        logging.info("form data %s", self.cleaned_data)
        sendgrid_mail(
            from_email=self.cleaned_data["email"],
            to_emails=os.environ.get("ENVELOPE_EMAIL_RECIPIENTS"),
            subject=self.cleaned_data["subject"],
            html_content=self.cleaned_data["message"],
        )
