from django.shortcuts import render, redirect
import requests
from branch.models import branchDetail

# Create your views here.
def newInvester(request):
	if request.method == "POST":
		print request.POST
		return redirect('Coinvester',23)
	else:
		allBranch = branchDetail.objects.all()
		print "Invester Register"
		return render(request, "invester/investerPersionalInfo.html", {"allBranch":allBranch})

def coInvester(request, investerId):
	if request.method == 'POST':
		print request.POST
		return redirect('InvesterBanckDetail',investerId)
	else:
		print "Coinvester"
	return render(request, 'invester/investerCoinvester.html', {'investerId':investerId})

def investerBankDetail(request, investerId):
	if request.method == 'POST':
		print request.POST
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