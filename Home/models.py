from django.db import models

# Create your models here.

class home_page(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=600)
    
class about_me(models.Model):
    description_1 = models.CharField(max_length=200)
    description_2 = models.CharField(max_length=200)
    description_3 = models.CharField(max_length=200)
    description_4 = models.CharField(max_length=200)
    description_5 = models.CharField(max_length=200)
    description_6 = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    telegram_id = models.CharField(max_length=200)
    Resume = models.FileField(default="")

class my_resume(models.Model):
    description_7 = models.CharField(max_length=200)
    