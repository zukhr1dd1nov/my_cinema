import re
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from main.models import ContactModel


class ContactModelForm(forms.ModelForm):

    def clean_phone(self):
        data = str(self.cleaned_data.get('phone'))
        if not re.match(r"9[^26]\d{7}", data):
            raise ValidationError(_("Введите реальный номер!"))
        return data

    class Meta:
        model = ContactModel
        exclude = ['created_at']