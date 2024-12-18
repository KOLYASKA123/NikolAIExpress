from .forms import ProductFilterForm

def product_filter_form(request):
    form = ProductFilterForm(request.GET or None)
    return {'product_filter_form': form}