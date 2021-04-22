from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False, blank=True, null=True)
    objects = models.Manager()
     
def __str__(self):
        return self.title

class User(AbstractUser):
    email = models.EmailField(verbose_name='email', max_length=255, unique=True)
    Mobile = models.CharField(null=True, max_length=255)
    REQUIRED_FIELDS = ['username', 'Mobile', 'first_name', 'last_name']
    USERNAME_FIELD = 'email'

    def get_username(self):
        return self.email

class phoneModel(models.Model):
    Mobile = models.IntegerField(User, blank=False, default=False)
    isVerified = models.BooleanField(blank=False, default=False)
    counter = models.IntegerField(default=0, blank=False)
    
    def __str__(self):
        return str(self.Mobile)

