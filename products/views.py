from django.shortcuts import render
from django.views import ListView
from .models import Product


class ProductListView(ListView):
    queryset = Product.objects.all()  # query everything

# identical functional based view


def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, 'product/product_list_view.html', context)
