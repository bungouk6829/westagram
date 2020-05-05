from django.db import models
from django.utils import timezone

class Comment(models.Model):
	text = models.CharField(max_length=1000)
	create_date = models.DateTimeField(auto_now_add=True)
