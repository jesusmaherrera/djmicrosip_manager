from django.conf.urls import url
from clients import views

urlpatterns = [
	url(r'^getmykey/(?P<username>\w+)/(?P<computername>\w+)/(?P<macaddress>\w+)/$', views.GetMyKey.as_view()),
]
