from django.shortcuts import render
import requests

# Create your views here.
def dashboardHome(request):
	if request.method == "GET":
		print "dashboard"
	return render(request, "dashboard/dashboard.html", {})