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
  user_district = models.ForeignKey(District, on_delete=models.CASCADE)



class Center(models.Model):
  center_district = models.ForeignKey(District, on_delete=models.CASCADE)
  center_name = models.CharField(max_length=100)
  center_slots = models.IntegerField()

  def __str__(self):
    return f'{self.center_name} has {self.center_slots} slots'