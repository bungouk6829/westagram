from django.db import models


class Account(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField(max_length=100)
	phone_number = models.CharField(max_length=20)
	password = models.CharField(max_length=100)

