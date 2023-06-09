from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Domain(models.Model):
    d_name = models.CharField(max_length=200)
    d_desc = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.d_name
    

class Events(models.Model):
    e_name = models.CharField(max_length=200)
    e_desc = models.TextField(null=True,blank=True)
    e_image = models.ImageField(null=True,blank=True,default="default.jpg")
    

    def __str__(self):
        return self.e_name
    
    def imageURL(self):
        try:
            img = self.e_image.url
        except:
            img = 'static/images/default.jpg'

        return img


class Topic(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name



class Room(models.Model):
    host = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    topic = models.ForeignKey(Topic,on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=200)
    desc = models.TextField(null=True , blank=True)
    # email = models.EmailField(max_length=75)
    participants = models.ManyToManyField(User,related_name='participants', blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['-updated' , '-created']

    def __str__(self):
        return self.name

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['-updated' , '-created']

    def __str__(self):
        return self.body[0:50]