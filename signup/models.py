from django.db import models
from django.contrib.auth.models import User


class UserDetail(models.Model):
    SEX = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    gender = models.CharField(max_length=1, choices=SEX)
    email = models.EmailField()

    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)


# TODO: i think i might change the structure of my project; the form would just be one and the user can edit
#   those settings in their profile later.