from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=100, blank=True)
    name = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=130, blank=True)
    is_active = models.BooleanField(blank=True, default=True)
    is_staff = models.BooleanField(blank=True, default=False)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self): return self.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(
            user=instance, 
            email=instance.email, 
            username=instance.username,
            is_staff=instance.is_staff,
            is_active=instance.is_active,
        )
