from django.http.response import JsonResponse
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render
from django.db import IntegrityError
import json 
from django.urls import reverse
from django.views.decorators.csrf import ensure_csrf_cookie
from .models import District, Center, User_details
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import requests



# Create your views here.

@ensure_csrf_cookie
def py_api(request):
  if request.method == "POST":
    data = json.loads(request.body)
    district_id = data.get('id')
    district = District.objects.get(district_id = district_id)
    slots_dict = {}
    slots_dict_dose2 = {}
    names = []
   
    for i in range(len(data['centers']['centers'])):
      if data['centers']['centers'][i]['sessions'][0]['min_age_limit'] == 18:
        names.append(data['centers']['centers'][i]['name'])
        name = data['centers']['centers'][i]['name']
        session_id = data['centers']['centers'][i]['sessions'][0]['session_id']
        slots_dict[f'{name}'] = [data['centers']['centers'][i]['sessions'][0]['available_capacity_dose1'], session_id]
        slots_dict_dose2[f'{name}'] = [data['centers']['centers'][i]['sessions'][0]['available_capacity_dose2'], session_id]
        print(slots_dict[name][1])
    
    
    x = list(User_details.objects.filter(user_district=district).filter(dose_2=False).values_list('user', flat=True))   
    z = list(User_details.objects.filter(user_district=district).filter(dose_2=True).values_list('user', flat=True))
  
    user_emails = list(User.objects.filter(pk__in=x).values_list('email', flat=True))
    user_emails_dose2 = list(User.objects.filter(pk__in=z).values_list('email', flat=True))
  

    for name in slots_dict:
      if Center.objects.filter(center_name = name).exists():
        old_slots = list(Center.objects.filter(center_name = name).values_list('center_slots_dose1', flat=True))
        old_session_id = list(Center.objects.filter(center_name = name).values_list('session_id', flat=True))
        old_slots2 = list(Center.objects.filter(center_name = name).values_list('center_slots_dose2', flat=True))
        old_session_id2 = list(Center.objects.filter(center_name = name).values_list('session_id', flat=True))
        if old_slots[0] != slots_dict[name][0] and old_session_id != slots_dict[name][1]:
          Center.objects.filter(center_name = name).update(center_slots_dose1 = slots_dict[name][0])
          if slots_dict[name][0] > 0:
            subject = 'Slots available!'
            message = f'{slots_dict[name][0]} slots available in {name}. Visit https://selfregistration.cowin.gov.in to book.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = user_emails
            send_mail(subject, message, email_from, recipient_list)
        elif old_slots2[0] != slots_dict_dose2[name][0] and old_session_id2 != slots_dict_dose2[name][1]:
           Center.objects.filter(center_name = name).update(center_slots_dose2 = slots_dict_dose2[name][0])
           if slots_dict_dose2[name][0] > 0:
            subject = 'Dose 2 slots available!'
            message = f'{slots_dict_dose2[name][0]} slots available in {name}. Visit https://selfregistration.cowin.gov.in to book. Note: Second dose will be available only 12 weeks after you took your first dose.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = user_emails_dose2
            send_mail(subject, message, email_from, recipient_list)
        else:
          print('same value')
      else:
          new = Center(center_district = district, center_name = name, center_slots_dose1 = slots_dict[name][0], session_id=slots_dict[name][1])
          new2 = Center(center_district = district, center_name = name, center_slots_dose2 = slots_dict_dose2[name][0], session_id=slots_dict_dose2[name][1])
          new.save()
          new2.save()
          if slots_dict[name][0] > 0:
            subject = 'Slots available!'
            message = f'{slots_dict[name][0]} slots available in {name}. Visit https://selfregistration.cowin.gov.in to book.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = user_emails
            send_mail(subject, message, email_from, recipient_list)
          elif slots_dict_dose2[name][0] > 0:
            subject = 'Dose 2 slots available!'
            message = f'{slots_dict_dose2[name][0]} slots available in {name}. Visit https://selfregistration.cowin.gov.in to book. Note: Second dose will be available only 12 weeks after you took your first dose.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = user_emails_dose2
            send_mail(subject, message, email_from, recipient_list)

    return JsonResponse('ok', safe=False)
   
    
  else:
    return render(request, 'cowin_alert/index.html')


def user_dict(request):
  district_ids = list(District.objects.all().values_list('district_id', flat=True))
  return JsonResponse(district_ids, safe=False)


def register(request):
  if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "cowin_alert/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "cowin_alert/register.html", {
                "message": "Username already taken."
            })
        return render(request, 'cowin_alert/thank_you.html')
  else:
      headers = {'User-agent': 'Safari/14.1 (macOS 11.3.1; x64)'}
      response = requests.get('https://cdn-api.co-vin.in/api/v2/admin/location/states', headers=headers)
      states = response.json()
      for i in range(len(states['states'])):
        print(states['states'][i]['state_name'])
      return render(request, "cowin_alert/register.html", {
        'states': states['states'],
      })
  