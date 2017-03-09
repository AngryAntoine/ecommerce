from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

# Create your views here.

from .models import Product


class ProductDetailView(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data()
        print(context)
        return context


class ProductListView(ListView):
    model = Product



















# def product_detail_view_func(request, id):
#     # product_instance = get_object_or_404(Product, id=id)  # Product.objects.get(id=id)
#     try:
#         product_instance = get_object_or_404(Product, id=id)  # Product.objects.get(id=id)
#     except Product.DoesNoExist:
#         raise Http404
#     except:
#         raise Http404
#
#     template = 'products/product_detail.html'
#     context = {
#         'object': product_instance,
#     }
#     return render(request, template, context)
