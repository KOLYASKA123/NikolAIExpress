from datetime import datetime

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login
from accounts.models import CustomUser
from django.contrib.auth.models import User
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
            user: CustomUser = registration_form.save(commit=False)
            user.is_staff = False
            user.is_active = True
            user.is_superuser = False
            user.date_joined = datetime.now()
            user.last_login = datetime.now()
            user.save()
            
            login(request, user)
            return redirect('/')
        return render(
            request,
            template_name='registration/registration.html',
            context={
                'form': registration_form
            }
        )