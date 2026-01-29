# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    phone_number  = models.IntegerField(null=True, blank=True)
    username  = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Registration(models.Model):

    #__Registration_FIELDS__
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    first_password = models.CharField(max_length=255, null=True, blank=True)
    second_password = models.CharField(max_length=255, null=True, blank=True)

    #__Registration_FIELDS__END

    class Meta:
        verbose_name        = _("Registration")
        verbose_name_plural = _("Registration")



#__MODELS__END
