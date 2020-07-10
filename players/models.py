from django.db import models

# Create your models here.


class player(models.Model):
    name = models.CharField(max_length=50)
    history = models.TextField()
    image = models.ImageField(upload_to='player_image')

