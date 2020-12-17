from django import forms


class AuthenticateForm(forms.Form):
    username = forms.CharField(
        label="username",
        max_length=20
    )
    password = forms.CharField(
        max_length=10,
        widget=forms.PasswordInput
    )
