from datetime import datetime

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View, TemplateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from app.models import OrderItem
from .forms import RegistrationForm, UserUpdateForm
from django.contrib.auth import login
from accounts.models import CustomUser
from django.http import JsonResponse
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
    

class UserProfileView(LoginRequiredMixin, TemplateView):
    template_name = "registration/profile.html"
    success_url = reverse_lazy("profile")

    def get(self, request, *args, **kwargs):
        user_form = UserUpdateForm(instance=request.user)
        orders = self.request.user.orders
        return render(
            request, 
            self.template_name, 
            {
                "user_form": user_form, 
                "user_profile": request.user,
                "orders": orders
            }
        )

    def post(self, request, *args, **kwargs):
        user_form = UserUpdateForm(request.POST, request.FILES, instance=self.request.user)
        if user_form.is_valid():
            user_form.save()
        return redirect(self.success_url)


class UserDeleteView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        user = self.request.user
        user.delete()
        return JsonResponse({"message": "Аккаунт удалён"}, status=200)
