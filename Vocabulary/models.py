from django.db import models

class wordlist(models.Model):
    word = models.CharField(max_length=80)
    mean = models.CharField(max_length=80)
