from django import forms


class FeedbackForm(forms.Form):
    name = forms.CharField(
        label='Ваше имя',
        min_length=2,
        max_length=100,
        widget=forms.TextInput(
            attrs={'class': 'outline'}
        )
    )
    city = forms.CharField(
        label='Ваш город',
        min_length=2,
        max_length=100,
        widget=forms.TextInput(
            attrs={'class': 'outline'}
        )
    )
    job = forms.CharField(
        label='Ваш род занятий',
        min_length=2,
        max_length=100,
        widget=forms.TextInput(
            attrs={'class': 'outline'}
        )
    )
    gender = forms.ChoiceField(
        label='Ваш пол',
        choices=[
            ('1', 'Мужской'),
            ('2', 'Женский')],
        widget=forms.RadioSelect(
            attrs={'class': 'outline'}
        ),
        initial=1
    )
    internet = forms.ChoiceField(
        label='Вы пользуетесь интернетом',
        choices=(
            ('1', 'Каждый день'),
            ('2', 'Несколько раз в день'),
            ('3', 'Несколько раз в неделю'),
            ('4', 'Несколько раз в месяц')
        ),
        initial=1,
        widget=forms.Select(
            attrs={'class': 'outline'}
        )
    )
    notice = forms.BooleanField(
        label='Получать новости сайта на e-mail?',
        initial=False,
        required=False,
        widget=forms.CheckboxInput(
            attrs={'class': 'outline'}
        )
    )
    email = forms.EmailField(
        label='Ваш e-mail',
        min_length=7,
        widget=forms.EmailInput(
            attrs={'class': 'outline'}
        )
    )
    message = forms.CharField(
        label='Коротко о себе',
        widget=forms.Textarea(
            attrs={
                'rows': 12,
                'cols': 20
            }
        )
    )
