from django.db import models

# Create your models here.
class App_Home_DB(models.Model):
  name = models.CharField(max_length=255)
  email = models.EmailField(max_length=255)
  phoneNumber = models.IntegerField()