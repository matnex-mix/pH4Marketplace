# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.utils import timezone

from django.db import models

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.CharField(max_length=500, blank=True)
    bio = models.CharField(max_length=1000, blank=True)
    slogan = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.user.username

class Gig(models.Model):
    CATEGORY_CHOICES = (
        ("SS", "Scripts & Software"),
        ("GD", "Graphics & Design"),
        ("WM", "Web Marketing"),
        ("V", "Videos"),
        ("M", "Music")
    )

    title = models.CharField(max_length=500)
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES)
    description = models.CharField(max_length=1000)
    price = models.IntegerField(default=6)
    photo = models.FileField(upload_to='gigs', blank=False)
    status = models.BooleanField(default=True)
    user = models.ForeignKey(User)
    create_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Purchase(models.Model):
    gig = models.ForeignKey(Gig)
    buyer = models.ForeignKey(User)
    time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.gig.title

class Review(models.Model):
    gig = models.ForeignKey(Gig)
    user = models.ForeignKey(User)
    content = models.CharField(max_length=500)

    def __str__(self):
        return self.content
