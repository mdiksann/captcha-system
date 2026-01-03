from django import forms
from captcha.fields import CaptchaField

class MyLoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    captcha = CaptchaField()