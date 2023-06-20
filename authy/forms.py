from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
# from django.contrib.auth.forms import UserCreationForm
import re


class CustomCreateUserForm(forms.Form):
    # first_name = forms.CharField(widget=forms.TextInput(), required=True)
    # last_name = forms.CharField(widget=forms.TextInput(), required=True)
    email = forms.EmailField(widget=forms.EmailInput(), required=True)
    password1 = forms.CharField(widget=forms.PasswordInput(), required=True)
    password2 = forms.CharField(widget=forms.PasswordInput(), required=True)

    def get_username(self):
        email = self.cleaned_data['email']
        username = email.split('@')[0]

        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError('Email has been used')
        return email

    def clean(self):
        super(CustomCreateUserForm, self).clean()
        password = self.cleaned_data.get('password1')
        confirm_password = self.cleaned_data.get('password2')
        char_check = re.compile('[~}<>!@#$%^&*(){_+\:;.],')

        if password != confirm_password:
            self.errors['password'] = self.error_class(
                ["Password does not match."])
            return self.cleaned_data

        # if any([chr.isdigit() for chr in password]) and any([chr.isupper() for chr in password]):
        #     pass
        # else:
        #     self.errors['password'] = self.error_class(
        #         ['Password does not meet the required'])

        return self.cleaned_data

    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.get_username(),
            email=self.cleaned_data['email'].lower(),
            password=self.cleaned_data['password1'],
        )
        return user
