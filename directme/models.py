from django.db import models
from django.utils import timezone

class DriverJob(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    clientid = models.ForeignKey( 'Client', on_delete=models.CASCADE,)

    driverid = models.ForeignKey ('Driver',on_delete=models.CASCADE,)

    instructions = models.TextField(max_length=500, blank=True, default='No Instructions')
    isdelivered = models.BooleanField(default=False)
    timeofdelivery = models.DateTimeField(auto_now_add=True)


class Driver(models.Model):
    name = models.CharField(max_length=100)
    phone= models.CharField(max_length=100)
    address = models.CharField(max_length=300)

    def __str__(self):
        return self.name

class Client(models.Model):
    name = models.CharField(max_length=100)
    phone= models.CharField(max_length=100)
    address = models.CharField(max_length=300)
    clientlattude= models.CharField(max_length=100)
    clientlogitute= models.CharField(max_length=100)

    def __str__(self):
        return self.name
