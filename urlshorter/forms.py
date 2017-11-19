from django import forms
from .models import *


class UrlsForm(forms.ModelForm):
        class Meta:
            model = Url
            exclude = [""]

        def __init__(self, *args, **kwargs):
            super(UrlsForm, self).__init__(*args, **kwargs)
            self.fields['Code'].widget.attrs['readonly'] = True
            self.fields['Code'].widget.attrs['onclick'] = "this.select()"
