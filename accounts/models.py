from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.db import models

class User(AbstractUser):
    is_head = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_public = models.BooleanField(default=False)

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    first_name=models.CharField(_("First Name"), max_length=150)
    last_name=models.CharField(_("Last Name"), max_length=150)
    phone=models.CharField(_("Phone Number"), max_length=100)
    