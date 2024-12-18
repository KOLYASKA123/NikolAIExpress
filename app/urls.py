from django.urls import path
from django.shortcuts import render
from . import views


urlpatterns = [
    path('', lambda request: render(request, 'about.html'), name='main'),
    path('videos/', lambda request: render(request, 'videos.html'), name='videos'),
    path('products/', views.ProductListView.as_view(), name='products'),

    path('cart/', views.CartItemListView.as_view(), name='cart'),
    path('cart/<int:pk>/delete-from-cart', views.ProductFromCartView.as_view(), name='delete_from_cart'),
    path('cart/create-order', views.OrderCreateView.as_view(), name='create_order'),

    path('products/<int:pk>', views.ProductDetailView.as_view(), name='product'),
    path('products/create', views.ProductFormView.as_view(), name='create_product'),
    path('products/<int:pk>/update', views.ProductUpdateView.as_view(), name='update_product'),
    path('products/<int:pk>/add-to-cart', views.ProductToCartView.as_view(), name='add_to_cart'),
    path('products/<int:pk>/add-to-last-order', views.AddProductToLastOrderView.as_view(), name='add_to_last_order'),
    path('products/<int:pk>/delete', views.ProductDeleteView.as_view(), name='delete_product'),
    path('products/<int:pk>/review', views.ProductReviewView.as_view(), name='create_review'),

    path('orders/', views.OrdersListView.as_view(), name='orders'),
    path('orders/<int:pk>/delete', views.OrderDeleteView.as_view(), name='delete_order'),
    path('orders/add-product/<int:product_id>', views.AddProductToOrderView.as_view(), name='add_order_item'),
    path('orders/remove-product/<int:order_item_id>', views.RemoveProductFromOrderView.as_view(), name='delete_order_item'),
    path('orders/cancel/<int:pk>', views.OrderCancelView.as_view(), name='cancel_order'),

    path('categories/<int:pk>', views.CategoryView.as_view(), name='categories'),

    path('partners/', lambda request: render(request, 'links.html'), name='partners'),
    path('feedback/', views.GlobalFeedbackView.as_view(), name='feedback'),

    path('news/', views.NewsListView.as_view(), name='news'),
    path('news/<int:pk>', views.NewsDetailView.as_view(), name='news_detail'),
    path('news/create', views.NewsCreateView.as_view(), name='create_post'),
    path('news/<int:pk>/update', views.NewsUpdateView.as_view(), name='update_post'),
    path('news/<int:pk>/delete', views.NewsDeleteView.as_view(), name='delete_post'),
]
