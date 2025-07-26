from django.shortcuts import render
from django.http import HttpResponse
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