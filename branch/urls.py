from django.conf.urls import url
from branch import views

urlpatterns = [
	url(r'^branch$', views.newBranch, name="NewBranch")
]