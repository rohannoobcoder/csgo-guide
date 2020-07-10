from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    #additional in user
    profile_pic = models.ImageField(upload_to='profile_pic')
    bday=models.DateField(auto_now=False)

    def __str__(self):
        return self.user.first_name