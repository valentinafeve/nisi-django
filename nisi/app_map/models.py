from django.db import models
from app_nuser.models import Nisi_user

# Location
class Location(models.Model):
    user = models.OneToOneField(Nisi_user, on_delete=models.CASCADE, primary_key=True)
    lng = models.DecimalField(max_digits=9, decimal_places=6, default=0.000)
    lat = models.DecimalField(max_digits=9, decimal_places=6, default=0.000)
    city_code = models.CharField(max_length=20, blank=True, default='BOG')
    # nisi_block = models.DecimalField(max_digits=10, decimal_places=6, default=0.000)
