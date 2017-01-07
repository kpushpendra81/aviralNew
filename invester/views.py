from django.shortcuts import render, redirect, HttpResponse
import json, datetime, urllib2, time, requests, os
from branch.models import branchDetail
from django.contrib.auth.models import User
from invester.models import investerDetails, coInvesterDetails, investerBankDetail, investerPlanDetail, investerPaymentDetail

# Create your views here.
def newInvester(request):
	if request.method == "POST":

		data = request.POST
		try:
			userId = User.objects.latest('id')
			userId = userId.id
		except:
			userId = 1

		userId = str(data['branch']) + str(userId + 1000) 
		user = User.objects.create_user(username = userId, password='123456')

		date_str = str(data['dateOfBirth'])
		format = '%m/%d/%Y'
		new_format = '%Y-%m-%d'

		investerDetail = investerDetails.objects.create(
			investerName 			= 	data['investerName'],
			fatherName 				= 	data['fatherName'],
			dateOfBirth 			= 	datetime.datetime.strptime(date_str, format).strftime(new_format),
			idProof 				= 	data['idProof'],
			idProofNo 				= 	data['idProofNo'],
			pan 					= 	data['pan'],
			occupation 				= 	data['occupation'],
			occupationSpecify 		= 	data['occuspecify'],
			address1 				= 	data['address1'],
			address2 				= 	data['address2'],
			address3 				= 	data['address3'],
			city 					= 	data['city'],
			state 					= 	data['state'],
			pin 					= 	data['pin'],
			correspondenceAddress1 	= 	data['correspondenceAddress1'],
			correspondenceAddress2 	= 	data['correspondenceAddress1'],
			correspondenceAddress3 	= 	data['correspondenceAddress1'],
			correspondenceCity 		= 	data['correspondenceCity'],
			correspondenceState		= 	data['correspondenceState'],
			correspondencePin		= 	data['correspondencePin'],
			contactno				= 	data['contactno'],
			email					= 	data['email'],
			marital					= 	data['marital'],
			branch					= 	branchDetail.objects.get(branchCode=data['branch']),
			user					= 	user
		)
		investerDetail.save()
		return redirect('Coinvester',investerDetail.investerId)

	else:

		allBranch = branchDetail.objects.all()
		return render(request, "invester/investerPersionalInfo.html", {"allBranch":allBranch})




def coInvester(request, investerId):
	if request.method == 'POST':
		data = request.POST

		date_str = str(data['codob'])
		format = '%m/%d/%Y'
		new_format = '%Y-%m-%d'

		coInvesterDetail = coInvesterDetails.objects.create(
			name 					= 	data['coname'],
			dob 					= 	datetime.datetime.strptime(date_str, format).strftime(new_format),
			idProof 				= 	data['coidProof'],
			idProofNo 				= 	data['coidProofNo'],
			pan 					= 	data['copan'],
			relation 				= 	data['corelation'],
			address1 				= 	data['address1'],
			address2 				= 	data['address2'],
			address3 				= 	data['address3'],
			city 					= 	data['city'],
			state 					= 	data['state'],
			pin 					= 	data['pin'],
			correspondenceAddress1 	= 	data['correspondenceAddress1'],
			correspondenceAddress2 	= 	data['correspondenceAddress1'],
			correspondenceAddress3 	= 	data['correspondenceAddress1'],
			correspondenceCity 		= 	data['correspondenceCity'],
			correspondenceState		= 	data['correspondenceState'],
			correspondencePin		= 	data['correspondencePin'],
			contact					= 	data['contactno'],
			email					= 	data['email'],
			marital					= 	data['marital'],
			invester				= 	investerDetails.objects.get(pk=investerId)
		)
		coInvesterDetail.save()
		return redirect('InvesterBanckDetail',investerId)
	else:
		print "Coinvester"
	return render(request, 'invester/investerCoinvester.html', {'investerId':investerId})




def investerDetail(request, investerId):
	if request.method == 'POST':
		data = request.POST
		data = investerDetails.objects.get(pk=data['investerId'])
		response_data = {
			"address1": data.address1,
			"address2": data.address2,
			"address3": data.address3,
			"city": data.city,
			"state": data.state,
			"pin": data.pin,
			"is_success": True
		}
		return HttpResponse(json.dumps(response_data), content_type="application/json")
	else:
		return render(request, 'invester/investerDetail.html', {'investerId':investerId})

def investerBank(request, investerId):
	if request.method == 'POST':
		data = request.POST
		print data
		
		date_str = str(data['createdAt'])
		format = '%m/%d/%Y'
		new_format = '%Y-%m-%d'

		bankDetail = investerBankDetail.objects.create(
			payeeName		=	data['payeeName'],
			bankName		=	data['bankName'],
			accountNumber 	=	data['accountNumber'],
			ifsc			= 	data['ifsc'],
			accountType		=	data['accountType'],
			branchAddress	=	data['branchAddress'],
			bankCity		=	data['bankCity'],
			branchState		=	data['branchState'],
			bankPin			=	data['bankPin'],
			createdAt		=	datetime.datetime.strptime(date_str, format).strftime(new_format),
			invester		=	investerDetails.objects.get(pk=investerId)
		)
		bankDetail.save()
		return redirect('InvesterDetail',investerId)

	else:
		print 'invester Bank Detail'
	return render(request, 'invester/investerBankDetail.html', {})

def investerAgreement(request):
	if request.method == 'POST':
		print request.POST
	else:
		print 'invester agreement'
	return render(request, 'invester/investerAgreement.html', {})


def investerList(request):

	if request.method == 'POST':
		print request.POST
	else:
		print 'Investr List'

	return render(request, 'invester/investerList.html', {})