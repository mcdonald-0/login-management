import random
from django.db import models
from django.contrib.auth.models import User


class UserDetail(models.Model):
    SEX = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    first_name = models.CharField(max_length=60)
    middle_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    gender = models.CharField(max_length=1, choices=SEX)
    email = models.EmailField()
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)


class WebDetail(models.Model):
    user = models.OneToOneField(User, null=True, default=User, on_delete=models.CASCADE)
    username = models.CharField(max_length=60)
    password = models.CharField(max_length=60)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.username
