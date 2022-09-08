from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def main_page(request):
    return HttpResponse('Hello! ')

def create_message(request):
    return HttpResponse('Vfds')

def base_html(request):
    return render(request, 'myapp1/index.html')

def staffs_html(request):
    return render(request, 'myapp1/staffs.html')

def heroes_html(request):
    return render(request, 'myapp1/heroes.html')
