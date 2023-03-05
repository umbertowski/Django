from django.template.context_processors import request
from django.urls import path

from . import views

urlpatterns = [
    path('', views.my_view, name='index'),
]