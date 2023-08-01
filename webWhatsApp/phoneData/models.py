from django.db import models
class PhoneData(models.Model):
    phoneNumber = models.IntegerField(max_length=8)
    article= models.CharField(max_length=5000,null=True)
# Create your models here.
