from django.urls import path
from . import views

urlpatterns = [
    path('py_api', views.py_api, name='py_api')
   
]
