from __future__ import unicode_literals

from django.db import models

# Create your models here.
class branchDetail(models.Model):
	branchID = models.AutoField(primary_key=True)
	branchCode = models.CharField(max_length=255, null=False)
	branchName = models.CharField(max_length=255, null=True, default="Aviral")
