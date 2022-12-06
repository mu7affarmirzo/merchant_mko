from django.db import models
from django.contrib.auth.models import User


class MerchantProfile(models.Model):
    user = models.OneToOneField(User, related_name='merchant_prof', on_delete=models.CASCADE)
    merchant_key = models.CharField(max_length=255, blank=True)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.user.username)
