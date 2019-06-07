from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Product


class ProductFeaturedListView(ListView):
    template_name = "products/list.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all().featured()


class ProductFeaturedDetailView(DetailView):
    # queryset = Product.objects.all()  # query everything
    template_name = "products/featured-detail.html"
    # class based view approach of define context, override get_context_data method
    # def get_object(self, *args, **kwargs):
    #     request = self.request
    #     pk = self.kwargs.get('pk')
    #     instance = Product.objects.get_by_id(pk)
    #     if instance is None:
    #         raise Http404('Product not found')
    #     return instance

    def get_queryset(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        return Product.objects.featured()


class ProductListView(ListView):
    # queryset = Product.objects.all()  # query everything
    template_name = "products/list.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()

    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProductListView, self).get_context_data(
    #         *args, **kwargs)
    #     print(context.get('product_list'))
    #     for key in context.get('product_list'):
    #         self.local_product_list.append(key)
    #     return context

        # identical functional based view


def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, 'products/list.html', context)


class ProductDetailSlugView(DetailView):
    queryset = Product.objects.all()
    template_name = "products/detail.html"

    def get_objects(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')

        try:
            instance = Product.objects.get(Product, slug=slug, active=True)
        except Product.DoesNotExist:
            raise Http404("Product doesn't exist")
        except Product.MultipleObjectsReturned:
            queryset = Product.objects.filter(slug=slug, active=True)
            return queryset.first()
        except:
            raise Http404("Uhhhmmm")
        return instance


class ProductDetailView(DetailView):
    # queryset = Product.objects.all()  # query everything
    template_name = "products/detail.html"
    # class based view approach of define context, override get_context_data method
    # def get_object(self, *args, **kwargs):
    #     request = self.request
    #     pk = self.kwargs.get('pk')
    #     instance = Product.objects.get_by_id(pk)
    #     if instance is None:
    #         raise Http404('Product not found')
    #     return instance

    def get_queryset(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        return Product.objects.filter(pk=pk)


def product_detail_view(request, pk=None, *args, **kwargs):
    instance = Product.objects.get_by_id(pk)
    if instance is None:
        raise Http404('Product not found')
    # key ward arguments are dictionary object, if you type /products-detail-fbv/2, print { 'pk': '2' }
    # try:
    #     pk = id
    #     instance = get_object_or_404(Product, pk=pk)
    # except Product.DoesNotExist:
    #     print('no product here')
    #     raise Http404("Product doesn't exist")
    # except:
    #     print('huh?')

    # qs = Product.objects.get_by_id(id=pk)
    # print(qs)
    # if qs.count() == 1:
    #     instance = qs.first()
    # else:
    #     raise Http404("Product doesn't exist")

    context = {
        'object': instance
    }
    return render(request, 'products/detail.html', context)
