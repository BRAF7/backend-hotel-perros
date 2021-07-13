from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=50)
    number = models.IntegerField()
    date = models.DateTimeField(max_length=20)
    diasEstancia = models.IntegerField()
    
    def __str__(self):
        return self.name