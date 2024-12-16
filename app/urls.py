from django.urls import path
from django.shortcuts import render
from . import views


urlpatterns = [
    path('', lambda request: render(request, 'about.html'), name='main'),
    path('videos/', lambda request: render(request, 'videos.html'), name='videos'),
    path('products/', views.ProductListView.as_view(), name='products'),
    path('products/<int:pk>', views.ProductDetailView.as_view(), name='product'),
    path('products/create', views.ProductFormView.as_view(), name='create_product'),
    path('products/<int:pk>/review', views.ProductReviewView.as_view(), name='create_review'),
    path('partners/', lambda request: render(request, 'links.html'), name='partners'),
    path('feedback/', views.GlobalFeedbackView.as_view(), name='feedback'),
]
