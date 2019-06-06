from django.conf.urls import url

from .views import (
    ProductListView,
    # product_list_view,
    # ProductDetailView,
    # product_detail_view,
    # ProductFeaturedDetailView,
    # ProductFeaturedListView,
    ProductDetailSlugView
)  # class view

urlpatterns = [
    ### product urls ###
    url(r'^products/$', ProductListView.as_view()),
    # slug url
    url(r'^products/(?P<slug>[\w-]+)$', ProductDetailSlugView.as_view()),
]
