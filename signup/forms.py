from django import forms
from django.contrib.auth.models import User


class UserCreateForm(forms.ModelForm):
    first_name = forms.CharField(
        max_length=60,
        min_length=3,
        label="",
        widget=forms.TextInput(attrs={'placeholder': 'First name'})
    )
    last_name = forms.CharField(
        max_length=60,
        min_length=3,
        label="",
        widget=forms.TextInput(attrs={'placeholder': 'Last name'})
    )
    gender = forms.ChoiceField(
            choices=(
                ('M', 'Male'),
                ('F', 'Female')
            ),
            label=""
        )
    email = forms.EmailField(
        label='',
        widget=forms.TextInput(attrs={'placeholder': 'Email'})
    )
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
    password_confirmation = forms.CharField(
        max_length=30,
        min_length=6,
        label="",
        widget=forms.PasswordInput(attrs={'placeholder': 'Password confirmation'})
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'gender', 'email', 'username', 'password', 'password_confirmation']


class UserLoginForm(forms.ModelForm):
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
