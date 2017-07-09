# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib import admin
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from collab.models import Technology
from collab.models import Project
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    picture = models.ImageField(blank=True)
    city = models.CharField(max_length=50)
    # state = models.CharField(max_length=50)
    zip = models.CharField(max_length=15)
    technologies = models.ManyToManyField(Technology, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    experience = models.TextField(max_length=500, blank=True)
    availability = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return unicode(self.user.username)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()


class Request(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipient')
    message = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return 'From: ' + unicode(self.sender) + ' | ' + unicode(self.project)


# class RequestInline(admin.TabularInline):
#     model = Request
#     extra = 1


class Platform(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Social(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    platform = models.ForeignKey(Platform)
    url = models.URLField()

    def __str__(self):
        return self.platform + ': ' + self.url


class SocialInline(admin.TabularInline):
    model = Social
    extra = 1
