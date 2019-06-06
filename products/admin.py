from django.contrib import admin
# import all your models
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'slug']

    class Meta:
        model = Product


# Register your models here!
admin.site.register(Product)
