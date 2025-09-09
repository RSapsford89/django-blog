from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.

class Bass(models.Model):
    manufacturer = models.CharField(max_length=200)
    bass_name = models.CharField(max_length=128)
    no_strings = models.PositiveSmallIntegerField(validators=[MaxValueValidator(12)])
    blurb = models.TextField()
    dateTime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.bass_name