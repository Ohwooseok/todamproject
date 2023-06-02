from django.db import models

class user(models.Model):
    userID = models.CharField(max_length=64, verbose_name='유저 ID')
    password = models.CharField(max_length=64, verbose_name='비밀번호')
