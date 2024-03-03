from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=20)
    branch=models.CharField(max_length=10)
    perc=models.FloatField()


 
