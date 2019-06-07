from django.conf.urls import url

from .views import (
    ProductListView,
    ProductDetailSlugView
)  # class view

urlpatterns = [
    ### product urls ###
    url(r'^$', ProductListView.as_view(), name='list'),
    # slug url
    url(r'^(?P<slug>[\w-]+)/$',
        ProductDetailSlugView.as_view(), name='detail'),
]
