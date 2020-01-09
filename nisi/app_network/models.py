from django.db import models
from app_nuser.models import Nisi_user

class Relation(models.Model):
    follower = models.ForeignKey(Nisi_user, on_delete=models.CASCADE, related_name='%(class)s_requests_follower')
    follows = models.ForeignKey(Nisi_user, on_delete=models.CASCADE, related_name='%(class)s_rqeuests_follows')
