from django.urls import path
from . import views

urlpatterns = [
    path('py_api', views.py_api, name='py_api'),
    path('user_dict', views.user_dict, name='user_dict'),
    path('register', views.register, name='register'),
    path('districts',views.districts, name='districts'), 

    
    

   
   
]
