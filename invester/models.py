from __future__ import unicode_literals

import os
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from advisor.models import advisorDetail
from decimal import Decimal
from plans.models import investerPlanDetail, advisorPlanDetail
from branch.models import branchDetail
from django.core.validators import MaxValueValidator, MinValueValidator

accountChoices = (

		('0', 'CURRENT'),
		('1', 'SAVING'),
		('2', 'SINGLE BIZ'),
		('3', 'JOINT ACCOUNT')
)

class investerDetails(models.Model):

	investerId 				= 	models.AutoField(primary_key=True)
	investerName 			= 	models.CharField(max_length=256, null=True, default="")
	fatherName 				= 	models.CharField(max_length=256, null=True, default="")
	dateOfBirth 			= 	models.DateTimeField(auto_now_add=False, auto_now=True)
	idProof 				= 	models.CharField(max_length=256, null=True, default="")
	idProofNo 				= 	models.CharField(max_length=256, null=True, default="")
	pan 					= 	models.CharField(max_length=256, null=True, default="")
	occupation 				= 	models.CharField(max_length=256, null=True, default="")
	occupationSpecify 		= 	models.CharField(max_length=256, null=True, default="")
	address1 				= 	models.CharField(max_length=255, null=True, default="")
	address2 				= 	models.CharField(max_length=255, null=True, default="")
	address3 				= 	models.CharField(max_length=255, null=True, default="")
	city 					= 	models.CharField(max_length=255, null=True, default="")
	state 					= 	models.CharField(max_length=255, null=True, default="")
	pin 					= 	models.CharField(max_length=6, null=True, default="000000")
	correspondenceAddress1 	= 	models.CharField(max_length=255, null=True, default="")
	correspondenceAddress2 	= 	models.CharField(max_length=255, null=True, default="")
	correspondenceAddress3 	= 	models.CharField(max_length=255, null=True, default="")
	correspondenceCity 		= 	models.CharField(max_length=255, null=True, default="")
	correspondenceState		= 	models.CharField(max_length=255, null=True, default="")
	correspondencePin		= 	models.CharField(max_length=255, null=True, default="")
	contactno				= 	models.CharField(max_length=10, null=True, default="")
	email					= 	models.EmailField(max_length=255, null=True, default="")
	marital					= 	models.CharField(max_length=255, null=True, default="")
	createdAt				= 	models.DateTimeField(auto_now_add=True, auto_now=False)
	updatedAt				= 	models.DateTimeField(auto_now_add=False, auto_now=True)
	branch					= 	models.ForeignKey(branchDetail, to_field='branchID', on_delete=models.CASCADE, null=True)
	user					= 	models.OneToOneField(User, on_delete=models.CASCADE, null=True)

	def __unicode__(self):

		return self.investerName


class coInvesterDetails(models.Model):

	coInvesterId 			= 	models.AutoField(primary_key=True)
	name 					= 	models.CharField(max_length=255, null=True)
	dob 					= 	models.DateTimeField(auto_now_add=True, auto_now=False)
	idProof 				= 	models.CharField(max_length=255, null=True)
	idProofNo 				= 	models.CharField(max_length=255, null=True)
	pan 					= 	models.CharField(max_length=255, null=True)
	relation 				= 	models.CharField(max_length=255, null=True)
	address1 				= 	models.CharField(max_length=255, null=True)
	address2 				= 	models.CharField(max_length=255, null=True)
	address3 				= 	models.CharField(max_length=255, null=True)
	city 					= 	models.CharField(max_length=255, null=True)
	state 					= 	models.CharField(max_length=255, null=True)
	pin 					= 	models.CharField(max_length=6, null=True)
	correspondenceAddress1 	= 	models.CharField(max_length=255, null=True)
	correspondenceAddress2 	= 	models.CharField(max_length=255, null=True)
	correspondenceAddress3 	= 	models.CharField(max_length=255, null=True)
	correspondenceCity 		= 	models.CharField(max_length=255, null=True)
	correspondenceState		= 	models.CharField(max_length=255, null=True)
	correspondencePin		= 	models.CharField(max_length=6, null=True)
	contact					= 	models.CharField(max_length=10, null=True)
	email 					= 	models.EmailField(max_length=255, null=True)
	marital 				= 	models.CharField(max_length=255, null=True)
	createdAt 				= 	models.DateTimeField(auto_now_add=True, auto_now=False)
	updatedAt 				= 	models.DateTimeField(auto_now_add=False, auto_now=True)
	invester 				= 	models.ForeignKey(investerDetails, to_field='investerId', on_delete=models.CASCADE, null=True)

	def __unicode__(self):

		return self.sellerName

class investerBankDetail(models.Model):

	investerBankId 		= 	models.AutoField(primary_key=True)
	payeeName 			= 	models.CharField(max_length=255, null=True)
	bankName 			= 	models.CharField(max_length=255, null=True)
	accountNumber 		= 	models.CharField(max_length=255, null=True)
	ifsc 				= 	models.CharField(max_length=255, null=True)
	accountType 		= 	models.CharField(max_length=20, choices=accountChoices)
	branchAddress 		= 	models.CharField(max_length=255, null=True)
	bankCity 			= 	models.CharField(max_length=255, null=True)
	branchState 		= 	models.CharField(max_length=255, null=True)
	bankPin 			= 	models.CharField(max_length=255, null=True)
	createdAt 			= 	models.DateTimeField(auto_now_add=True, auto_now=False)
	updatedAt 			= 	models.DateTimeField(auto_now_add=False, auto_now=True)
	invester 			= 	models.ForeignKey(investerDetails, to_field='investerId', on_delete=models.CASCADE, null=True)

	def __unicode__(self):

		return self.accountNo

class investerPlanDetail(models.Model):

	investerPlanId 	= 	models.AutoField(primary_key=True)
	branchCode 		= 	models.CharField(max_length=256, null=True)
	investPeriod 	= 	models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)], default=1)
	installmentMode = 	models.CharField(max_length=256)
	createdAt 		= 	models.DateTimeField(auto_now_add=True, auto_now=False)
	updatedAt 		= 	models.DateTimeField(auto_now_add=False, auto_now=True)
	advisorPlan 	= 	models.ForeignKey(advisorPlanDetail, to_field='PlanDetailId', on_delete=models.CASCADE, null=True)
	plan 			= 	models.ForeignKey(investerPlanDetail, to_field='PlanDetailId', on_delete=models.CASCADE, null=True)
	advisor			= 	models.ForeignKey(advisorDetail, to_field='advisorId', on_delete=models.CASCADE, null=True)
	invester		= 	models.ForeignKey(investerDetails, to_field='investerId', on_delete=models.CASCADE, null=True)

	def __unicode__(self):

		return self.branchCode

class investerPaymentDetail(models.Model):

	paymentId 		= 	models.AutoField(primary_key=True)
	investAmount	= 	models.DecimalField(max_digits=12, decimal_places=2, default=Decimal('0.00'))
	paymode			= 	models.CharField(max_length=100)
	checkno 		= 	models.CharField(max_length=100, default='')
	createdAt 		= 	models.DateTimeField(auto_now_add=True, auto_now=False)
	updatedAt 		= 	models.DateTimeField(auto_now_add=False, auto_now=True)
	investerPlan	= 	models.ForeignKey(investerPlanDetail, to_field='investerPlanId', on_delete=models.CASCADE, null=True)
	invester		= 	models.ForeignKey(investerDetails, to_field='investerId', on_delete=models.CASCADE, null=True)

