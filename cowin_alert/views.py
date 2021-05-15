from django.shortcuts import render
import json 
from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse

# Create your views here.
@csrf_exempt
def index(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        
        for k, v in data.items():
            for k1, v1 in v.items():
                for k2 in v1:
                    capacity = v1
        

        for i in range(len(capacity)):
            if capacity[i]['sessions'][0]['min_age_limit'] == 18:
                #above18 = capacity[i]['name']
                #print(f'{above18} is for above 18')
                if capacity[i]['sessions'][0]['available_capacity'] != 0:
                    n = capacity[i]['name']
                    ava_slots = capacity[i]['sessions'][0]['available_capacity']
                    print (f'{n} => {ava_slots}')
                    subject = 'Slots available!'
                    message = f'{ava_slots} available at {n}'
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list = ['rshan.ali@gmail.com']
                    send_mail(subject, message, email_from, recipient_list
                        )
                else:
                    print('no slots')
            #else:
                #above45 = capacity[i]['name']
                #print(f'{above45} is for 45 and above')    
       

        return JsonResponse({'message': 'done'}, status = 201)
        
    else:
        return render(request, "cowin_alert/index.html")