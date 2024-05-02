from django.urls import path
from django.shortcuts import render
from . import views


urlpatterns = [
    path('', lambda request: render(request, 'about.html'), name='main'),
    path('products/', views.ProductListView.as_view(), name='products'),
    path('products/<int:pk>', views.ProductDetailView.as_view(), name='product'),
    path('products/<int:pk>/feedback', views.ProductFeedbackView.as_view(), name='create_feedback'),
    path('partners/', lambda request: render(request, 'links.html'), name='partners'),
    path('feedback/', views.GlobalFeedbackView.as_view(), name='feedback'),
]
