# from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('all_prod', views.all_prod, name = 'all_prod'),
    path('add_prod', views.add_prod, name = 'add_prod'),
    path('remove_prod', views.remove_prod, name = 'remove_prod'),
    path('remove_prod/<int:prod_id>', views.remove_prod, name='remove_prod'),
    path('filter_prod', views.filter_prod, name = 'filter_prod'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
]
