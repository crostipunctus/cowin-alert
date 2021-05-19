from django.http.response import JsonResponse
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
import requests, threading, time, datetime
from datetime import date
import schedule, json 
from django.views.decorators.csrf import csrf_exempt
from .models import Slots



# Create your views here.

@csrf_exempt
def py_api(request):
  if request.method == "POST":
    data = json.loads(request.body)
    my_email = ['rshan.ali@gmail.com']
    all_emails = ['sumonach@gmail.com', 'avneeshn@gmail.com']
    slots_dict = {}
    
    for i in range(len(data['centers']['centers'])):
      if data['centers']['centers'][i]['sessions'][0]['min_age_limit'] == 45:
        names = data['centers']['centers'][i]['name']
        if data['centers']['centers'][i]['sessions'][0]['available_capacity_dose1'] == 0:
          slots = data['centers']['centers'][i]['sessions'][0]['available_capacity_dose1']
          slots_dict[f'{names}'] = slots
          
        else: 
          print('no slots')

    new = Slots(data = slots_dict)
    new.save()

    return JsonResponse('ok', safe=False)
   
    
  else:
    return render(request, 'cowin_alert/index.html')


