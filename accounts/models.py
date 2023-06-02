from django.db import models

class user(models.Model):
    userID = models.CharField(max_length=64, verbose_name='유저 ID')
    password = models.CharField(max_length=64, verbose_name='비밀번호')

class Vocabulary(models.Model):
    name = models.CharField(max_length=100)
    mean = models.CharField(max_length=100)