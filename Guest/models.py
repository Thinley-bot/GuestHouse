import email
from xml.parsers.expat import model
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Guesthouse(models.Model):
    #h_id,h_name,owner ,location,rooms
    name = models.CharField(max_length=30,default="Thinley")
    owner = models.CharField(max_length=20)
    location = models.CharField(max_length=50)
    state = models.CharField(max_length=50,default="Chukha")
    country = models.CharField(max_length=50,default="Bhutan")
    def __str__(self):
        return self.name


class Rooms(models.Model):
    ROOM_STATUS = ( 
    ("1", "available"), 
    ("2", "not available"),    
    ) 

    ROOM_TYPE = ( 
    ("1", "Quad"), 
    ("2", "Doubles"),
    ("3","Single"),    
    ) 

    #type,no_of_rooms,capacity,prices
    room_type = models.CharField(max_length=50,choices = ROOM_TYPE)
    capacity = models.IntegerField()
    price = models.IntegerField()
    size = models.IntegerField()
    guest = models.ForeignKey(Guesthouse, on_delete = models.CASCADE)
    status = models.CharField(choices =ROOM_STATUS,max_length = 15)
    roomnumber = models.IntegerField()
    def __str__(self):
        return self.guest.name

class Reservation(models.Model):

    check_in = models.DateField(auto_now =False)
    check_out = models.DateField()
    room = models.ForeignKey(Rooms, on_delete = models.CASCADE)
    guest = models.ForeignKey(User, on_delete= models.CASCADE)
    
    booking_id = models.CharField(max_length=100,default="null")
    def __str__(self):
        return self.guest.username


class Contact(models.Model):
    name = models.CharField(max_length=30)
    number = models.EmailField(null=False, blank=True,max_length=30)
    subject=models.TextField()
    def __str__(self):
        return self.name