from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from .models import Product
from .forms import ProductForm, RawProductForm
# Create your views here.

def home(request):
    return render(request, 'index.html', {})

def contacts(request):
    return render(request, 'contacts.html', {})

def about(request):
    mycontext = {
        'my_text': 'This is about us',
        'my_number': 123,
        'my_list': [1, 2, 3, 4, 5],
    }
    return render(request, 'about.html', mycontext)

def product_detail(request, my_id):
    # obj = Product.objects.get(id=my_id)
    # obj = get_object_or_404(Product, id=my_id)  # Alternative way to get the object
    try:
        obj = Product.objects.get(id=my_id)
    except Product.DoesNotExist:
        raise Http404
    context = {
        'object': obj,

    }
    return render(request, 'product_detail.html', context)

# def product_create(request):
#     my_form = RawProductForm()
#     if request.method == "POST":
#         my_form = ProductForm(request.POST)
#         if my_form.is_valid():
#             Product.objects.create(**my_form.cleaned_data)
            
#     context = {
#         'form': my_form,      
#     }
#     return render(request, 'product_create.html', context)


def product_create(request):
    my_form = ProductForm(request.POST or None)  # Use POST data if available
    if my_form.is_valid():
        my_form.save()  # Save the form data to the database

            
    context = {
        'form': my_form,      
    }
    return render(request, 'product_create.html', context)

def product_delete(request, my_id):
    obj = get_object_or_404(Product, id=my_id)
    if request.method == "POST":
        obj.delete()  # Delete the object if the request method is POST
        return redirect('../../../')

    context = {
        'object': obj,
    }
    return render(request, 'product_delete.html', context)  # Render a confirmation page 


def product_list(request):
    object_list = Product.objects.all()

    context = {
        'objects': object_list,
    }

    return render(request, 'product_list.html', context)