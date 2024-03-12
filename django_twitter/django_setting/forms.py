from django import forms
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django_accounts.models import CustomUser


class ChangeUsernameForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name']
        labels = {
            'first_name': 'New First Name',
            'last_name': 'New Last Name',  # You can customize the label here
        }


class ChangeEmailForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['email']
        labels = {
            'email': 'New Email',  # Customize the label here
        }


class ChangeMobileNumberForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['phone_number']
        labels = {
            'phone_number': 'New Mobile Number',  # Customize the label here
        }


class PasswordChangeForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = []  # We don't need to specify fields here since they are handled by the parent class

