from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class User(AbstractUser):
    username = models.CharField(blank=True, null=True, max_length=100)
    email = models.EmailField(unique=True, max_length=100)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return '{}'.format(self.email)


class Naver(models.Model):
    name = models.CharField(max_length=100)
    admission_date = models.DateField(default=timezone.now)
    birthdate = models.DateField()
    job_role = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Project(models.Model):
    name = models.CharField(max_length=100)
    navers = models.ManyToManyField(Naver, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
