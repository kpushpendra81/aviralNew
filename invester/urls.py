from django.conf.urls import url
from invester import views

urlpatterns = [
	url(r'^newinvester$', views.newInvester, name="NewInvester"),	
	url(r'^coinvester/(?P<investerId>\d+)/$', views.coInvester, name="Coinvester"),
	url(r'^investerbankdetail/(?P<investerId>\d+)/$', views.investerBankDetail, name='InvesterBanckDetail'),
	url(r'^investeragreement$', views.investerAgreement, name='InvesterAgreement'),
	url(r'^investerlist$', views.investerList, name="investerList"),	
]