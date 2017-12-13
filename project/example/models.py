# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
GENDER_CHOICES = (
('M', 'Male'),
('F', 'Female'),
)

class DataRow(models.Model):
    date = models.DateField(blank=False)
    gender = models.CharField(max_length = 1, choices = GENDER_CHOICES, blank=False)
    favorite_number = models.IntegerField(blank=False)
