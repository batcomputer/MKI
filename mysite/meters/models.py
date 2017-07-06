# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Energy(models.Model):

    date = models.CharField(max_length=20)
    time = models.CharField(max_length=15)
    energy = models.CharField(max_length=50)

    def __str__(self):

        return self.energy
        