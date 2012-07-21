# -*-*- encoding: utf-8 -*-*-
from django import forms
from django.utils.translation import ugettext_lazy as _


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100,
            label=_('Subject'))
    message = forms.CharField(widget=forms.Textarea,
            label=_('Message'))
    sender = forms.EmailField(required=False,
            label=_('Your e-mail address'))
    cc_myself = forms.BooleanField(required=False,
            label=_('Send me a copy'))

    def clean_message(self):
        message = self.cleaned_data['message']
        num_words = len(message.split())
        if num_words < 4:
            raise forms.ValidationError("Not enough words!")
        return message
