from django import forms
from .models import SnsMessageModel,Image

class SnsMessageForm(forms.Form):
<<<<<<< HEAD
    message = forms.CharField(label='Message',widget=forms.Textarea(attrs={'cols': '80', 'rows': '10'}))
    picture = forms.ImageField(label='picture')

class SnsCommentForm(forms.Form):
    message = forms.CharField(label='Message',widget=forms.Textarea(attrs={'cols': '80', 'rows': '10'}))
=======
    message = forms.CharField(label='Message')

class SnsCommentForm(forms.Form):
    message = forms.CharField(label='Message')
>>>>>>> origin/master

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['picture']