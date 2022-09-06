from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def main_page(request):
    return HttpResponse('Hello! ')

def create_message(request):
    return HttpResponse('Vfds')

def first_html(request):
    return render(request, 'base.html')
