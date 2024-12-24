from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.conf import settings
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox

class ContactForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit("submit", "Send Email"))

    sender = forms.CharField(max_length=256, label="From")
    email = forms.EmailField(max_length=256)
    subject = forms.CharField(max_length=256)
    message = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(attrs=dict(cols=19, rows=10, placeholder="2000 character limit")),
    )
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)

    def send_email(self):
        self._send_email(
            recipients=getattr(settings, "ENVELOPE_EMAIL_RECIPIENTS", []),
            subject=self.cleaned_data["subject"],
            body=self.cleaned_data["message"],
            reply_to=[self.cleaned_data["email"]],
            from_email=self.cleaned_data["email"],
        )

    def _send_email(self, recipients, subject, body, reply_to, from_email):
        print(
            recipients,
            subject,
            body,
            reply_to,
            from_email
        )
