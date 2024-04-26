from django.urls import path
from django.shortcuts import render
from . import views


urlpatterns = [
    path('about/', lambda request: render(request, 'about.html'), name='about'),
    path('partners/', lambda request: render(request, 'links.html'), name='partners'),
    path('feedback/', views.FeedbackView.as_view(), name='feedback'),
]
