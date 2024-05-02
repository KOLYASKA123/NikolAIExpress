from datetime import datetime

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import RegistrationForm
# Create your views here.


class RegistrationView(View):
    def get(self, request):
        registration_form = RegistrationForm()  # создание объекта формы для ввода данных нового пользователя
        return render(
            request,
            template_name='registration/registration.html',
            context={
                'form': registration_form,
            }
        )

    def post(self, request):
        registration_form = RegistrationForm(request.POST)
        if registration_form.is_valid():  # валидация полей формы
            reg_f = registration_form.save(commit=False)
            reg_f.is_staff = False
            reg_f.is_active = True
            reg_f.is_superuser = False
            reg_f.date_joined = datetime.now()
            reg_f.last_login = datetime.now()
            reg_f.save()
            return redirect('/')
        return render(
            request,
            template_name='registration/registration.html',
            context={
                'form': registration_form
            }
        )
