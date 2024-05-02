from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm
from django import forms
from django.utils.translation import gettext as _


class AuthForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(
            attrs={
                'placeholder': _('Имя пользователя'),
                'autofocus': True
            }
        )
    )
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': _('Пароль'),
                'autocomplete': 'current-password',
            }
        ),
    )


class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Пароль",
                "autocomplete": "new-password"
            }
        ),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Повторите пароль",
                "autocomplete": "new-password"
            }
        ),
        help_text=_("Enter the same password as before, for verification."),
    )

    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'placeholder': 'Имя пользователя'
                }
            )
        }
