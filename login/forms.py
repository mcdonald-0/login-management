from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=30,
        min_length=2,
        label="",
        widget=forms.TextInput(attrs={'placeholder': 'username'})
    )
    password = forms.CharField(
        max_length=30,
        min_length=6,
        label="",
        widget=forms.PasswordInput(attrs={'placeholder': 'password'})
    )

