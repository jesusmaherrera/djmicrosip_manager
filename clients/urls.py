from django.conf.urls import url
from clients import views

urlpatterns = [
	url(r'^getmykey/(?P<username>[a-zA-Z0-9.-]+)/(?P<computername>[a-zA-Z0-9.-]+)/(?P<macaddress>\w+)/$', views.GetMyKey.as_view()),
]
