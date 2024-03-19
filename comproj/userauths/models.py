from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100)


    USER_FIELD = "email"
    REQUIRED_FIELDS = ['username']

    def __self__(self):
        return self.username