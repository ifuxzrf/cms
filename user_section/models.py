# from django.db import models
# from django.contrib.auth.models import User
# from django.db.models.signals import post_save
#
#
# # Create your models here.
# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     description = models.TextField(max_length=51200)
#     scope = models.IntegerField(default=100)
#
#
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         profile, created = UserProfile.objects.get_or_create(user=instance)
#
#
# post_save.connect(create_user_profile, sender=User)
#
#
