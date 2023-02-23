from django.db import models
from django.utils import timezone
#from django.contrib.auth.models import User

class User(models.Model):
    user_id = models.IntegerField(primary_key='True')
    username = models.CharField( max_length=100)
    contact = models.IntegerField()
    email = models.EmailField(max_length=25)
    passwd = models.CharField(max_length=25)
    usertype = models.CharField(max_length=25)

class Equipment(models.Model):
    equ_name = models.CharField(max_length=100)
    description = models.TextField()
    available = models.BooleanField(default=True)
    daily_rate = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField()

class Rental(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)
    renter_name = models.CharField(max_length=100)
    renter_phone = models.CharField(max_length=20)
    renter_email = models.EmailField()
    total_price = models.IntegerField()


    # def save(self, *args, **kwargs):
    #     +
    #     self.total_price = (self.end_date - self.start_date).days * self.equipment.daily_rate
    #     super().save(*args, **kwargs)

class FloorPlanRequirement(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    min_squarefeet = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    max_squarefeet = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    rooms = models.IntegerField(blank=True, null=True)
    bathrooms = models.IntegerField(blank=True, null=True)
    site_image = models.ImageField()
    hometype= models.CharField(max_length=25)

class Worker(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    joining_date =models.DateTimeField(null=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    skill = models.CharField(max_length=100, blank=True, null=True)

class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

class Shift(models.Model):
    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)

class JobAssignment(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)

class ShiftAssignment(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE)
    date = models.DateField(null=True) 