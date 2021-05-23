from django.db import models
from django.contrib.auth.models import User

class Recordatorio(models.Model):
	"""Model definition for Recordatorio."""
	"""Modelo para la estructura de los recordatorios"""

	title = models.CharField(max_length=20)
	memo = models.TextField(blank=True)
	created = models.DateTimeField(auto_now_add=True)
	completed = models.DateTimeField(null=True, blank=True)
	important = models.BooleanField(default=False)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	
	# title
	# memo
	# created
	# datecompleted
	# important
	# user

	def __str__(self):
		return self.title