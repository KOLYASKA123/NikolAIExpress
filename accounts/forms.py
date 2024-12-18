from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.forms import (
    AuthenticationForm, 
    UsernameField, 
    UserCreationForm
)
from django import forms
from django.utils.translation import gettext as _

from accounts.models import CustomUser


class AuthForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(
            attrs={
                'placeholder': _('Электронная почта'),
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
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'Электронная почта'
            }
        )
    )
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
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'placeholder': 'Имя пользователя'
                }
            )
        }

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'avatar', 'status')
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'placeholder': 'Имя пользователя'
                }
            ),
            'status': forms.Textarea(
                attrs={
                    'placeholder': 'Статус'
                }
            )
        }

class PasswordChangeForm(forms.Form):
    email = forms.EmailField(label="Email", required=True, widget=forms.EmailInput(attrs={'placeholder': 'Электронная почта'}))
    old_password = forms.CharField(label="Старый пароль", widget=forms.PasswordInput(attrs={'placeholder': 'Старый пароль'}), required=True)
    new_password = forms.CharField(label="Новый пароль", widget=forms.PasswordInput(attrs={'placeholder': 'Новый пароль'}), required=True)

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("Пользователь с таким email не найден.")
        return email
