from datetime import datetime

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views.generic import View
# Create your views here.


def registration(request):

    if request.method == "POST": # после отправки формы
        regform = UserCreationForm(request.POST)

        if regform.is_valid():  # валидация полей формы

            reg_f = regform.save(commit=False)  # не сохраняем автоматически данные формы

            reg_f.is_staff = False  # запрещен вход в административный раздел

            reg_f.is_active = True  # активный пользователь

            reg_f.is_superuser = False  # не является суперпользователем

            reg_f.date_joined = datetime.now()  # дата регистрации

            reg_f.last_login = datetime.now()  # дата последней авторизации

            reg_f.save()  # сохраняем изменения после добавления данных

            return redirect('home')  # переадресация на главную страницу после регистрации

    else:
        regform = UserCreationForm()  # создание объекта формы для ввода данных нового пользователя
        return render(
            request,
            template_name='app/registration.html',
            context= {
                'regform': regform,  # передача формы в шаблон веб-страницы
                'year': datetime.now().year,
            }
        )