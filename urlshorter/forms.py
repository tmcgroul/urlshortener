from django import forms
from .models import *


class UrlsForm(forms.ModelForm):
        class Meta:
            model = Url
            exclude = [""]
