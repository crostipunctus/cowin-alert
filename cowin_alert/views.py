from django.http.response import JsonResponse
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
import requests, threading, time, datetime
from datetime import date
<<<<<<< HEAD
import schedule, json 
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

@csrf_exempt
def py_api(request):
  if request.method == "POST":
    data = json.loads(request.body)
    
    emails = ['rshan.ali@gmail.com', 'sumonach@gmail.com', 'avneeshn@gmail.com']
    
    for i in range(len(data['centers']['centers'])):
      if data['centers']['centers'][i]['sessions'][0]['min_age_limit'] == 18:
        names = data['centers']['centers'][i]['name']
        print(names)
        if data['centers']['centers'][i]['sessions'][0]['available_capacity'] > 0:
          slots = data['centers']['centers'][i]['sessions'][0]['available_capacity']
          print(f'{slots} slots available at {names}')
          #print(slots)
          av_slots = data['centers']['centers'][i]['sessions'][0]['available_capacity'] 
          subject = 'Slots available!'
          message = f'{av_slots} available at {names}. Visit https://selfregistration.cowin.gov.in to book.'
          email_from = settings.EMAIL_HOST_USER
          recipient_list = emails
          send_mail(subject, message, email_from, recipient_list)
        else: 
          print('no slots')
      
    
    return JsonResponse('ok', safe=False)
   
    
  else:
    return render(request, 'cowin_alert/index.html')

=======


# Create your views here.

def apicall(district_id):
  headers = {'user-agent': 'Safari/14.1 (Macintosh; Intel macOS 11_3_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
  d = date.today()
  today = d.strftime("%d-%m-%Y")
  response = requests.get(f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={district_id}&date={today}", headers=headers)
  print(response.status_code)
  data = response.json()
  
  emails = ['rshan.ali@gmail.com', 'sumonach@gmail.com', 'avneeshn@gmail.com']
  for i in range(len(data['centers'])):
    if data['centers'][i]['sessions'][0]['min_age_limit'] == 18:
      names = data['centers'][i]['name']
      if data['centers'][i]['sessions'][0]['available_capacity_dose1'] > 0:
        slots = data['centers'][i]['sessions'][0]['available_capacity']
        print(names)
        print(slots)
        av_slots = data['centers'][i]['sessions'][0]['available_capacity_dose1'] 
        subject = 'Slots available!'
        message = f'{av_slots} available at {names}. Visit https://selfregistration.cowin.gov.in to book.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['rshan.ali@gmail.com',]
        send_mail(subject, message, email_from, recipient_list)
      else: 
        print('no slots')
    else:
      print('no slots for 18-44')
      

  


def py_api(request):
  
  apicall(726)
  
  return HttpResponse('ok')
>>>>>>> ae1c879ac53e3525237b76ae4e79151fb5115ada

