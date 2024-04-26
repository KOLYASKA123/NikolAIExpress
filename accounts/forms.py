from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django import forms
from django.utils.translation import gettext as _

class AuthForm(AuthenticationForm):
    username = UsernameField(
        label=_('Имя пользователя'),
        widget=forms.TextInput(
            attrs={
                'autofocus': True
            }
        )
    )
    password = forms.CharField(
        label=_('Пароль'),
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'current-password'
            }
        ),
    )
