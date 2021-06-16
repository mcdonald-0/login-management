from django import forms
from .models import UserDetail
from django.contrib.auth.models import User


class UserDetailForm(forms.ModelForm):
    first_name = forms.CharField(
            max_length=60,
            min_length=3,
            label="",
            widget=forms.TextInput(attrs={'placeholder': 'First name'})
        )
    SEX = (
            ('M', 'Male'),
            ('F', 'Female'),
        )
    last_name = forms.CharField(
        max_length=60,
        min_length=3,
        label="",
        widget=forms.TextInput(attrs={'placeholder': 'Last name'})
    )
    # gender = forms.ChoiceField(
    #         choices=SEX,
    #         label=""
    #     )
    email = forms.EmailField(
        label='',
        widget=forms.TextInput(attrs={'placeholder': 'Email'})
    )

    class Meta:
        model = UserDetail
        fields = ['first_name', 'last_name', 'email']


class UserCreateForm(forms.ModelForm):
    username = forms.CharField(
        max_length=30,
        min_length=2,
        label="",
        widget=forms.TextInput(attrs={'placeholder': 'Username'})
    )
    password = forms.CharField(
        max_length=30,
        min_length=6,
        label="",
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'})
    )

    class Meta:
        model = User
        fields = ['username', 'password']



