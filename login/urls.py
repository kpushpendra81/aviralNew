from django.conf.urls import url
from login import views

urlpatterns = [
	url(r'^', views.login, name="Login"),	
	url(r'^forgot', views.forgotPassword, name="ForgotPassword"),	
]