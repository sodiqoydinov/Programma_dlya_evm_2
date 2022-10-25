from pyexpat import model
from django.db import models

# Create your models here.


class UsersInfo(models.Model):
    fio = models.CharField(max_length=150)
    pol = models.CharField(max_length=20)

    def __str__(self):
        return self.fio
