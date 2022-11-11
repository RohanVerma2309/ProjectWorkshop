from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Image

class ImageForm(forms.ModelForm):
 class Meta:
  model = Image
  fields = '__all__'
  labels = {'photo':''}


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
