__author__ = 'MillerB'

from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(required=True,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))


class SignupForm(forms.Form):
    username = forms.CharField(max_length=30, required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    email = forms.EmailField(max_length=50, required=True,
                             widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(required=True,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    confirm = forms.CharField(required=True,
                              widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))