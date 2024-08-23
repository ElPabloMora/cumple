from django.db import models

class UserProfile(models.Model):
    profile_picture = models.ImageField(upload_to='profile_pics/')
