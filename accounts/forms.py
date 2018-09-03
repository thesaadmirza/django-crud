from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import Profile,User
class HeadSignupForm(UserCreationForm):
   
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_head = True
        user.save()
        profile = Profile.objects.create(user=user)
        return user