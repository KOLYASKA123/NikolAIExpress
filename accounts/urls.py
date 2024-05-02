from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views, forms

urlpatterns = [
    path(
        'registration/',
        views.RegistrationView.as_view(),
        name='registration'
    ),
    path(
        'login/',
        LoginView.as_view(
            template_name='registration/login.html',
            authentication_form=forms.AuthForm,
        ),
        name='login'
    ),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
]
