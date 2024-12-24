from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from django import forms
from django.conf import settings
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox

class ContactForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["captcha"].label = False

    sender = forms.CharField(max_length=256)
    email = forms.EmailField(max_length=256)
    subject = forms.CharField(max_length=256)
    message = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(attrs=dict(cols=19, rows=10, placeholder="2000 character limit")),
    )
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)

    helper = FormHelper()
    helper.add_input(Submit("submit", "Send Email"))
    helper.layout = Layout(
        Field("sender"),
        Field("email"),
        Field("subject"),
        Field("message"),
        Field('captcha', style="border: none; padding: 0px"),
    )

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
