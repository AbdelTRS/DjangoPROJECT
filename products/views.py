from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Product
from .forms import ProductForm

# Create your views here.


# Retrieve product list
def product_list(request):
    products = Product.objects.all()
    return render(request, "products/product_list.html", { "products": products,})


# Retrieve a single product
def product_detail(request, id):  
    context ={}

    # add the dictionary during initialization
    context["data"] = Product.objects.get(id = id)
    context["range"] = range(1, context["data"].quantity+1)
    return render(request, "products/product_detail.html", context)


# Update a single product
def product_update(request, id):
    quantityChose = request.POST.get('quantity')
    obj = get_object_or_404(Product, id = id)
    Product.objects.filter(id = id).update(quantity = obj.quantity - int(quantityChose))
    obj.refresh_from_db()
    return HttpResponseRedirect('/products')