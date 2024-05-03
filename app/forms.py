from django import forms
from .models import Feedbacks, Products, Categories, SubCategories, Brands


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
        label = 'Ваш пол',
        choices=[
            ('1', 'Мужской'),
            ('2', 'Женский')],
        widget=forms.RadioSelect(
            attrs={'class': 'outline', 'placeholder': 'Ваш пол'}
        ),
        initial=1
    )
    internet = forms.ChoiceField(
        label='Вы совершаете покупки в интернете',
        choices=(
            ('1', 'Каждый день'),
            ('2', 'Несколько раз в день'),
            ('3', 'Несколько раз в неделю'),
            ('4', 'Несколько раз в месяц'),
            ('5', 'Ещё реже')
        ),
        initial=1,
        widget=forms.Select(
            attrs={'class': 'outline', 'placeholder': 'Вы совершаете покупки в интернете'}
        )
    )
    notice = forms.BooleanField(
        label='Получать новости сайта на e-mail',
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
                'placeholder': 'Ващ отзыв или проблема, с которой вы столкнулись'
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


class MultipleFileInput(forms.ClearableFileInput):
    template_name = 'widgets/multiple_file_input.html'

    def value_from_datadict(self, data, files, name):
        upload = super().value_from_datadict(data, files, name)
        if not upload:
            return None
        return [item for item in upload if item]


class ProductForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Название'}
        )
    )
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={'placeholder': 'Описание'}
        )
    )
    preview_image = forms.FileField(
        label='Превью товара',  # Добавляем явное название поля
        widget=forms.ClearableFileInput(  # Используем ClearableFileInput для возможности удаления файлов
            attrs={'placeholder': 'Превью товара'},
        ),
        required=False  # Поле необязательное
    )
    category = forms.ModelChoiceField(
        label='Категория',
        queryset=SubCategories.objects.all(),
        widget=forms.Select(
            attrs={'placeholder': 'Категория'}
        )
    )
    brand = forms.ModelChoiceField(
        label='Бренд',
        queryset=Brands.objects.all(),
        widget=forms.Select(
            attrs={'placeholder': 'Бренд'}
        )
    )
    price = forms.DecimalField(
        label='Цена',  # Добавляем явное название поля
        widget=forms.NumberInput(
            attrs={'placeholder': 'Цена'}
        )
    )

    class Meta:
        model = Products
        fields = ('name', 'description', 'preview_image', 'category', 'brand', 'price')
