from django.conf.urls import url
from clients import views

urlpatterns = [
	url(r'^clients/$', views.client_list),
	url(r'^clients/(?P<pk>[0-9]+)/$', views.client_detail),
]
