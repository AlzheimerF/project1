from django.urls import path
from .views import main_page, create_message, first_html

urlpatterns = [
    path('', main_page),
    path('fs/', first_html)
]