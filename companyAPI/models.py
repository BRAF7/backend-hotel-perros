from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=50)
    number = models.IntegerField(max_length=10)
    date = models.DateTimeField(max_length=20)