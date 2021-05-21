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
from .models import District
from django.contrib.auth.models import User



# Create your views here.

@csrf_exempt
def py_api(request):
  if request.method == "POST":
    data = json.loads(request.body)
    district_id = data.get('id')
    print(district_id)
    my_email = ['rshan.ali@gmail.com']
    all_emails = ['sumonach@gmail.com', 'avneeshn@gmail.com']
    slots_dict = {}
    
    for i in range(len(data['centers']['centers'])):
      if data['centers']['centers'][i]['sessions'][0]['min_age_limit'] == 18:
        names = data['centers']['centers'][i]['name']
        if data['centers']['centers'][i]['sessions'][0]['available_capacity_dose1'] == 0:
          slots = data['centers']['centers'][i]['sessions'][0]['available_capacity_dose1']
          slots_dict[f'{names}'] = slots
          
        else: 
          print('no slots')



    objs = Slots.objects.all()

    if objs:
      ob = Slots.objects.first()
      value = getattr(ob, 'data')
      print(value)
      if value == slots_dict:
        print('same values')
      else:
        Slots.objects.filter(pk=1).update(data=slots_dict)
        print('value updated')
        subject = 'Slots available!'
        message = f'{slots_dict}. Visit https://selfregistration.cowin.gov.in to book.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = my_email
        send_mail(subject, message, email_from, recipient_list)
      
    else:
      if slots_dict:
        new = Slots(data = slots_dict)
        new.save()
        slot_str = str(slots_dict)
        print(slot_str)
        subject = 'Slots available!'
        message = f'{slots_dict}. Visit https://selfregistration.cowin.gov.in to book.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = my_email
        send_mail(subject, message, email_from, recipient_list)
      else:
        print('no slots')
      


    return JsonResponse('ok', safe=False)
   
    
  else:
    return render(request, 'cowin_alert/index.html')


def user_dict(request):
  #emails = (User.objects.filter(is_active=True).values_list('email', flat=True))
  district_ids = list(District.objects.all().values_list('district_id', flat=True))
  
  print(district_ids)
  return JsonResponse(district_ids, safe=False)
