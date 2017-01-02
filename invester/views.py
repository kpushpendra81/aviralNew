from django.shortcuts import render
import requests

# Create your views here.
def newInvester(request):
	if request.method == "POST":
		print request.POST
	else:
		print "Invester Register"
	return render(request, "invester/newInvester.html", {})