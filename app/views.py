from django.shortcuts import render, redirect
from django.views.generic import View, ListView, DetailView, CreateView, DeleteView, UpdateView
from .forms import FeedbackForm, ProductFeedbackForm, ProductForm
from .models import Products, Feedbacks
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


class ProductListView(ListView):
    model = Products
    template_name = 'product_list.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Products
    template_name = 'product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ProductFeedbackForm()
        return context

class ProductFeedbackView(View):
    def post(self, request, pk):
        product = Products.objects.get(id=pk)
        form = ProductFeedbackForm(self.request.POST)
        if form.is_valid():
            Feedbacks.objects.create(
                product=product,
                user=self.request.user,
                text=form.cleaned_data['text'],
            )
        return redirect('product', pk=pk)



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
