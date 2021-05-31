from django.http.response import JsonResponse
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render
from django.db import IntegrityError
import json 
from django.urls import reverse
from django.views.decorators.csrf import ensure_csrf_cookie
from .models import District, Center, User_details, Slots, State
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
    #print(data)
    dose1_users = list(User_details.objects.filter(user_district=district).filter(dose_2=False).values_list('user', flat=True))   
    dose2_users = list(User_details.objects.filter(user_district=district).filter(dose_2=True).values_list('user', flat=True))
  
    dose1_user_emails = list(User.objects.filter(pk__in=dose1_users).values_list('email', flat=True))
    dose2_user_emails = list(User.objects.filter(pk__in=dose2_users).values_list('email', flat=True))

    for i in range(len(data['centers']['centers'])):
      for x in range(len(data['centers']['centers'][i]['sessions'])):
        if data['centers']['centers'][i]['sessions'][x]['min_age_limit'] == 18:
          center_id = data['centers']['centers'][i]['center_id']
          name = data['centers']['centers'][i]['name']
          print(center_id)
          print(name)
          session_id = data['centers']['centers'][i]['sessions'][x]['session_id']
          dose1 = data['centers']['centers'][i]['sessions'][x]['available_capacity_dose1']
          dose2 = data['centers']['centers'][i]['sessions'][x]['available_capacity_dose2']
          if Center.objects.filter(center_id=center_id).exists():
            center = Center.objects.get(center_id=center_id)
            if Slots.objects.filter(session_id=session_id).exists():
              print('session id exists')
            else:
              print('new slot added')
              new_slots = Slots(center_slots = center, slots_dose1 = dose1, slots_dose2 = dose2, session_id=session_id)
              new_slots.save()
              if dose1 > 0:
                subject = 'Slots available!'
                message = f'{dose1} slots available in {name}. Visit https://selfregistration.cowin.gov.in to book.'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = dose1_user_emails
                send_mail(subject, message, email_from, recipient_list)
              if dose2 > 0:
                subject = 'Dose 2 slots available!'
                message = f'{dose2} slots available in {name}. Visit https://selfregistration.cowin.gov.in to book. Note: Second dose will be available only 12 weeks after your first dose.'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = dose2_user_emails
                send_mail(subject, message, email_from, recipient_list)     
          else:
            new_center = Center(center_district=district, center_name=name, center_id=center_id)
            new_center.save()
            center1 = Center.objects.get(center_id=center_id)
            if Slots.objects.filter(session_id=session_id).exists():
              print('session id exists')
            else:
              new_slots = Slots(center_slots = center1, slots_dose1 = dose1, slots_dose2 = dose2, session_id=session_id)
              new_slots.save()
              if dose1 > 0:
                subject = 'Slots available!'
                message = f'{dose1} slots available in {name}. Visit https://selfregistration.cowin.gov.in to book.'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = dose1_user_emails
                send_mail(subject, message, email_from, recipient_list)
              if dose2 > 0:
                subject = 'Dose 2 slots available!'
                message = f'{dose2} slots available in {name}. Visit https://selfregistration.cowin.gov.in to book. Note: Second dose will be available only 12 weeks after your first dose.'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = dose2_user_emails
                send_mail(subject, message, email_from, recipient_list)     

    
    return JsonResponse('ok', safe=False)
   
    
  else:
    
    return render(request, 'cowin_alert/index.html')

    
    
def user_dict(request):
  users = User.objects.all()
  districts = list(User_details.objects.filter(user__in=users).values_list('user_district', flat=True))
  district_ids = list(District.objects.filter(id__in=districts).values_list('district_id', flat=True))
  return JsonResponse(district_ids, safe=False)
  


def register(request):
  if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        district = request.POST["district"]
        print(district)

        # Ensure password matches confirmation
        # password = request.POST["password"]
        # confirmation = request.POST["confirmation"]
        # if password != confirmation:
        #     return render(request, "cowin_alert/register.html", {
        #         "message": "Passwords must match."
        #     })

        # # Attempt to create new user
        # try:
        #     user = User.objects.create_user(username, email, password)
        #     user.save()
        # except IntegrityError:
        #     return render(request, "cowin_alert/register.html", {
        #         "message": "Username already taken."
        #     })
        return render(request, 'cowin_alert/thank_you.html')
  else:
      states = State.objects.all()
      return render(request, 'cowin_alert/register.html', {
        'states': states

      })
      


def districts(request):
  data = json.loads(request.body)
  state_name = data.get('state')
  state = State.objects.get(state_name=state_name)
  districts = list(District.objects.filter(state=state).values_list('district_name', flat=True))
  print(districts)
  return JsonResponse(districts, safe=False)


