from django.urls import path
from .views import main_page, create_message, base_html, staffs_html, heroes_html

urlpatterns = [
    path('', main_page),
    path('home/', base_html, name='home'),
    path('staffs/', staffs_html, name='staffs'),
    path('heroes/', heroes_html, name='heroes'),
]
