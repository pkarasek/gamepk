from django.db import models
from django.contrib.auth.models import User


class Character(models.Model):
    player = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    #user = models.OneToOneField(User, related_name="character", null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
