from django.urls import path
from .views import main_page, create_message, base_html

urlpatterns = [
    path('', main_page),
    path('home/', base_html, name='home'),
    # path('/staffs', )
]