from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import View, ListView, DetailView, CreateView, DeleteView, UpdateView

from accounts.models import CustomUser
from .forms import FeedbackForm, ProductReviewForm, ProductForm
from .models import CartItem, Category, Order, OrderItem, Product, Review
from django.utils import timezone
from django.contrib.auth.mixins import UserPassesTestMixin
# Create your views here.

class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser

    def handle_no_permission(self):
        return redirect('main')

class GlobalFeedbackView(View):

    def post(self, request):
        data = None
        gender = {
            '1': 'Мужчина',
            '2': 'Женщина'
        }
        internet = {
            '1': 'Каждый день',
            '2': 'Несколько раз в день',
            '3': 'Несколько раз в неделю',
            '4': 'Несколько раз в месяц'
        }
        form = FeedbackForm(self.request.POST)
        if form.is_valid():
            data = {
                'name': form.cleaned_data['name'],
                'city': form.cleaned_data['city'],
                'job': form.cleaned_data['job'],
                'gender': gender[form.cleaned_data['gender']],
                'internet': internet[form.cleaned_data['internet']],
                'notice': 'Да' if form.cleaned_data['notice'] else 'Нет',
                'email': form.cleaned_data['email'],
                'message': form.cleaned_data['message'],
            }
            form = None
        return render(request, 'pool.html', {'form': form, 'data': data})

    def get(self, request):
        form = FeedbackForm()
        return render(self.request, 'pool.html', {'form': form})


# class ProductCreateView(AdminRequiredMixin, CreateView):
#     model = Products
#     form_class = ProductForm
#     template_name = 'product_form.html'
#     success_url = '/products/'
#
#     def form_valid(self, form: ProductForm):
#
#         print(form.cleaned_data)
#         return redirect('products') #super().form_valid(form)

class ProductFormView(AdminRequiredMixin, View):
    def get(self, request):
        form = ProductForm()
        return render(request, 'product_form.html', {'form': form})

    def post(self, request):
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            return redirect('product', pk=product.id)
        return render(request, 'product_form.html', {'form': form})
    
class ProductUpdateView(AdminRequiredMixin, View):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        form = ProductForm(instance=product)
        return render(request, 'product_update_form.html', {'form': form, 'product': product})

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product', pk=product.id)
        return render(request, 'product_update_form.html', {'form': form, 'product': product})
    

class ProductToCartView(View):
    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        CartItem.objects.create(
            user=request.user,
            product=product,
        )
        return JsonResponse({'success': True, 'message': 'Товар добавлен в корзину'})
    
class ProductFromCartView(View):
    def post(self, request, pk):
        print(pk)
        CartItem.objects.filter(id=pk).first().delete()
        return redirect('cart')
    
class ProductDeleteView(AdminRequiredMixin, View):
    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        product.delete()
        return JsonResponse({'success': True, 'message': 'Товар удалён'})


class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'


class CartItemListView(ListView):
    model = CartItem
    template_name = 'cart.html'
    context_object_name = 'cart'
    
    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user).all()
    
class OrdersListView(ListView):
    model = Order
    template_name = 'orders.html'
    context_object_name = 'orders'

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user).all()
    

class OrderDeleteView(View):
    def post(self, request, pk):
        order = get_object_or_404(Order, pk=pk)
        order.delete()
        return redirect('orders')


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ProductReviewForm()
        return context
    

class AddProductToOrderView(View):
    def post(self, request, pk, product_id):
        user = CustomUser.objects.get(id=request.user.id)
        order = Order.objects.filter(user=user).order_by('-id').first()
        product = get_object_or_404(Product, pk=product_id)
        OrderItem.objects.create(
            order=order,
            product=product
        )
        return redirect('orders')
    

class RemoveProductFromOrderView(View):
    def post(self, request, order_item_id):
        order_item = get_object_or_404(OrderItem, pk=order_item_id)
        order_item.delete()
        return redirect('orders')


class ProductReviewView(View):
    def post(self, request, pk):
        product = Product.objects.get(id=pk)
        form = ProductReviewForm(self.request.POST)
        if form.is_valid():
            Review.objects.create(
                product=product,
                user=self.request.user,
                text=form.cleaned_data['text'],
            )
        return redirect('product', pk=pk)


class OrderCreateView(View):
    def post(self, request):
        cart_items = CartItem.objects.filter(user=request.user).all()
        order = Order.objects.create(
            user=request.user
        )
        order_items = []
        for cart_item in cart_items:
            order_items.append(OrderItem(
                product=cart_item.product,
                order=order,
            ))
        OrderItem.objects.bulk_create(order_items)
        cart_items.delete()
        return redirect('orders')
    
class CategoryView(ListView):
    
    def get(self, request, pk):
        if pk == 0:
            categories = Category.objects.filter(main_category=None).all()
            return render(request, 'categories.html', {'categories': categories})
        category = get_object_or_404(Category, pk=pk)
        if category.subcategories.count() == 0:
            return render(request, 'products.html', {'products': category.products.all()})
        return render(request, 'category.html', {'categories': category.subcategories.all()})


# class ProductUpdateView(UpdateView):
#     model = Products
#     template_name = 'product_form.html'
#     fields = '__all__'
#     success_url = '/products/'
#
#
# class ProductDeleteView(DeleteView):
#     model = Products
#     template_name = 'product_form.html'
#     success_url = '/products/'
