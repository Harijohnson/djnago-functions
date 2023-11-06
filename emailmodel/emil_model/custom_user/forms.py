from django import forms
from django.contrib.auth.models import User

class UserRegister(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput(),max_length=50)
    cpassword = forms.CharField(widget=forms.PasswordInput(),max_length=50)
    class Meta:
        model= User
        fields = ['username','email','password1','password2']



















