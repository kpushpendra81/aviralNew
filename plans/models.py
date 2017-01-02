from __future__ import unicode_literals

import os
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class investerPlanDetail(models.Model):

	PlanDetailId	= 	models.AutoField(primary_key=True)
	PlanName 		= 	models.CharField(max_length=10)
	planDuration	= 	models.IntegerField(validators=[MaxValueValidator(4), MinValueValidator(0)], default=0)
	interest 		= 	models.BooleanField(default=00.0)
	profit 			= 	models.BooleanField(default=00.0)
	createdAt 		= 	models.DateTimeField(auto_now_add=True, auto_now=False)
	updatedAt 		= 	models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self):

		return self.PlanName

class advisorPlanDetail(models.Model):

	PlanDetailId	= 	models.AutoField(primary_key=True)
	PlanName 		= 	models.CharField(max_length=10)
	planDuration	= 	models.IntegerField(validators=[MaxValueValidator(4), MinValueValidator(0)], default=0)
	interest 		= 	models.BooleanField(default=00.0)
	target 			= 	models.BooleanField(default=00.0)
	profit 			= 	models.BooleanField(default=00.0)
	createdAt 		= 	models.DateTimeField(auto_now_add=True, auto_now=False)
	updatedAt 		= 	models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self):

		return self.PlanName