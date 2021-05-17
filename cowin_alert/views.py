from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
import requests


# Create your views here.

def py_api(request):
  headers = {'user-agent': 'Safari/14.1 (Macintosh; Intel macOS 11_3_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
  response = requests.get("https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=294&date=17-05-2021", headers=headers)
  data = response.json()

  for i in range(len(data['centers'])):
    if data['centers'][i]['sessions'][0]['min_age_limit'] == 18:
      names = data['centers'][i]['name']
      if data['centers'][i]['sessions'][0]['available_capacity'] > 0:
        slots = data['centers'][i]['sessions'][0]['available_capacity']
        print(names)
        print(slots)
        av_slots = data['centers'][i]['sessions'][0]['available_capacity'] 
        subject = 'Slots available!'
        message = f'{av_slots} available at {names}'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['rshan.ali@gmail.com']
        send_mail(subject, message, email_from, recipient_list)


  return HttpResponse('done')