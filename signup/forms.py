from django import forms


class UserDetailForm(forms.Form):
    first_name = forms.CharField(
        max_length=60,
        min_length=3,
        label="",
        widget=forms.TextInput(attrs={'placeholder': 'First name'})
    )
    middle_name = forms.CharField(
        max_length=60,
        min_length=3,
        required=False,
        label="",
        widget=forms.TextInput(attrs={'placeholder': 'Middle name'})
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
    # TODO: I need to put a default of gender in this gender form
    gender = forms.ChoiceField(
        choices=SEX,
        label=""
    )
    email = forms.EmailField(
        label='',
        widget=forms.TextInput(attrs={'placeholder': 'Email'})
    )


class WebDetailForm(forms.Form):
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
