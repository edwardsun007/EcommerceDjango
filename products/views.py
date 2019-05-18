from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Product


class ProductListView(ListView):
    queryset = Product.objects.all()  # query everything
    template_name = "products/list.html"
    local_product_list = []
    # class based view approach of define context, override get_context_data method

    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView, self).get_context_data(
            *args, **kwargs)
        print(context.get('product_list'))
        for key in context.get('product_list'):
            self.local_product_list.append(key)
        return context

        # identical functional based view


def product_list_view(request):
    context = {
        'object_list': instance
    }
    return render(request, 'products/list.html', context)


class ProductDetailView(DetailView):
    queryset = Product.objects.all()  # query everything
    template_name = "products/detail.html"
    # class based view approach of define context, override get_context_data method

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(
            *args, **kwargs)
        print(context)
        context['abc'] = 123  # you can display abc by  {{abc}}
        return context
    # identical functional based view


def product_detail_view(request, pk=None, *args, **kwargs):
    # key ward arguments are dictionary object, if you type /products-detail-fbv/2, print { 'pk': '2' }
    print(kwargs)
    instance = get_object_or_404(Product, pk=pk)
    context = {
        'object': instance
    }
    return render(request, 'products/detail.html', context)
