from django.shortcuts import render
import requests
# Create your views here.


def newBranch(request):
	if request.method == "POST":
		print request.POST
	else:
		print "Add new branch"
	return render(request, 'branch/newBranch.html', {})