
from django.shortcuts import render, redirect
from django.http.response import HttpResponse, HttpResponseForbidden
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import time, requests, json, datetime
from hashlib import sha1
from django.contrib import messages

# Create your views here.
def forgotPassword(request):
	if request.method == "POST":
		print request.POST
	else:
		print "Login"
	return render(request, "login/forgotPass.html", {})


def login(request):

	if not request.user.is_authenticated():

		if request.method == "POST":

			username = request.POST['username']
			password = request.POST['password']
			try:

				user = User.objects.get(username=username)

				if user.is_superuser:

					seller = authenticate(username=user.username, password=password)

					if seller:
						if seller.is_active:
							login(request, seller)
							request.session['username'] = 'blue'
							return redirect(request.GET.get('next', 'Dashboard'))

					else:
						messages.error(request, "Incorrect username or password")
						return render(request, 'home.html', {'email': email})

				else:
					messages.error(request, "Incorrect username/password or user not registerd.")
					return render(request, 'home.html', {'email': email})

			except Exception, e:
				print e
				messages.error(request, "Incorrect username or password")
				return render(request, 'home.html', {'email': email})
		else:
			return render(request, "login/home.html")

	else:
		return redirect("Dashboard")