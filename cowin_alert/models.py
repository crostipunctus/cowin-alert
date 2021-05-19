from django.db import models

# Create your models here.

class Slots(models.Model):
  data = models.JSONField()

