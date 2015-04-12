from django.conf.urls import url
from clients import views

urlpatterns = [
	url(r'^getmykey/$', views.GetMyKey.as_view()),
]
