from django import forms

from ecoapp.models import SaveUrl


class PostForm(forms.ModelForm):
    class Meta:
        model = SaveUrl
        exclude = [" "]
