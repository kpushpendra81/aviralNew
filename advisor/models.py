from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class advisorDetail(models.Model):
	"""docstring for advisorDetail"""
	advisorId 		= models.AutoField(primary_key=True)
	name			= models.CharField(max_length=256, default='')
	user 			= models.OneToOneField(User, on_delete=models.CASCADE, null=True)

	def __init__(self, arg):
		super(advisorDetail, self).__init__()
		self.arg = arg


# Create your models here.
