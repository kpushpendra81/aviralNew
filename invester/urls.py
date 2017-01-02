from django.conf.urls import url
from invester import views

urlpatterns = [
	url(r'^newinvester$', views.newInvester, name="NewInvester"),	
]