from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Nisi_user(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    token = models.CharField(max_length=58, blank=True, default='')
    first_name = models.CharField(max_length=20, blank=True, default='')
    last_name = models.CharField(max_length=20, blank=True, default='')
    about = models.CharField(max_length=150, blank=True, default='')
    phone = models.CharField(max_length=20, blank=True, default='')
    email = models.CharField(max_length=20, blank=True, default='')
    picture_path = models.CharField(max_length=100, blank=True, default='')
    born_date = models.DateTimeField('date birth', blank=True, default='2000-01-01 01:10:10-00')
    rating = models.DecimalField(max_digits=4, decimal_places=3, default=3.000)

class SN(models.Model):
    user = models.ForeignKey(Nisi_user, on_delete=models.CASCADE)
    code = models.CharField(max_length=58, blank=True, default='')
    FACEBOOK = 'fb'
    TWITTER = 'tw'
    INSTAGRAM = 'ig'
    TELEGRAM = 'tg'
    SN_CHOICES = [
        (FACEBOOK, 'fb'),
        (TWITTER, 'tw'),
        (INSTAGRAM, 'ig'),
        (TELEGRAM, 'tg'),
    ]
    name = models.CharField(max_length=20, choices=SN_CHOICES, blank=True, default='')
    username = models.CharField(max_length=20, blank=True, default='')
    verified = models.BooleanField(default=False)

class Statistics(models.Model):
    user = models.OneToOneField(Nisi_user, on_delete=models.CASCADE)
    irated = models.IntegerField()
    ratedme = models.IntegerField()
