from django import forms
from .models import SnsMessageModel,Image

class SnsMessageForm(forms.Form):
    message = forms.CharField(label='Message')

class SnsCommentForm(forms.Form):
    message = forms.CharField(label='Message')

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['picture']