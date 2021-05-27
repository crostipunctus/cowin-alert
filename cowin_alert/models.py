from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class District(models.Model):
  district_name = models.CharField(max_length=100)
  district_id = models.IntegerField()

  def __str__(self):
    return f'{self.district_name} => {self.district_id}'

class User_details(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  user_district = models.ManyToManyField(District)
  dose_2 = models.BooleanField(default=False)



class Center(models.Model):
  center_district = models.ForeignKey(District, on_delete=models.CASCADE)
  center_name = models.CharField(max_length=100)
  
  def __str__(self):
    return f'{self.center_name}'

class Slots(models.Model):
  center_slots = models.ForeignKey(Center, on_delete=models.CASCADE)
  slots_dose1 = models.IntegerField(default=0, blank=True)
  slots_dose2 = models.IntegerField(default=0, blank=True)
  session_id = models.TextField(max_length=100)

  def __str__(self):
    return f'{self.session_id} => {self.center_slots} has {self.slots_dose1} dose one slots and {self.slots_dose2} dose two slots'



