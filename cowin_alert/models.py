from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class District(models.Model):
  district_id = models.IntegerField()
  user_district = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return f'{self.user_district} => {self.district_id}'

class Slots(models.Model):
  data = models.JSONField()
  slot_district = models.ForeignKey(District, on_delete=models.CASCADE)