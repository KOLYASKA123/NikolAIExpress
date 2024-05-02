from django import forms
from .models import Feedbacks


class FeedbackForm(forms.Form):
    name = forms.CharField(
        min_length=2,
        max_length=100,
        widget=forms.TextInput(
            attrs={'class': 'outline', 'placeholder': 'Ваше имя'}
        )
    )
    city = forms.CharField(
        min_length=2,
        max_length=100,
        widget=forms.TextInput(
            attrs={'class': 'outline', 'placeholder': 'Ваш город'}
        )
    )
    job = forms.CharField(
        min_length=2,
        max_length=100,
        widget=forms.TextInput(
            attrs={'class': 'outline', 'placeholder': 'Ваш род занятий'}
        )
    )
    gender = forms.ChoiceField(
        choices=[
            ('1', 'Мужской'),
            ('2', 'Женский')],
        widget=forms.RadioSelect(
            attrs={'class': 'outline', 'placeholder': 'Ваш пол'}
        ),
        initial=1
    )
    internet = forms.ChoiceField(
        choices=(
            ('1', 'Каждый день'),
            ('2', 'Несколько раз в день'),
            ('3', 'Несколько раз в неделю'),
            ('4', 'Несколько раз в месяц')
        ),
        initial=1,
        widget=forms.Select(
            attrs={'class': 'outline', 'placeholder': 'Вы пользуетесь интернетом'}
        )
    )
    notice = forms.BooleanField(
        initial=False,
        required=False,
        widget=forms.CheckboxInput(
            attrs={'class': 'outline', 'placeholder': 'Получать новости сайта на e-mail?'}
        )
    )
    email = forms.EmailField(
        min_length=7,
        widget=forms.EmailInput(
            attrs={'class': 'outline', 'placeholder': 'Ваш e-mail'}
        )
    )
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'outline',
                'rows': 12,
                'cols': 20,
                'placeholder': 'Коротко о себе'
            }
        )
    )


class ProductFeedbackForm(forms.Form):
    text = forms.CharField(

        max_length=500,
        widget=forms.Textarea(
            attrs={
                'cols': 50, 'rows': 10,
                'placeholder': 'Ваш отзыв',
            }
        )
    )
