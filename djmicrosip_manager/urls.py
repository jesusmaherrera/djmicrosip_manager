from django.conf.urls import patterns, include, url
from django.contrib import admin
from servers.models import Server
from applications.models import Application
from clients.models import Client
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username',)

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Routers provide an easy way of automatically determining the URL conf.
from companies.views import CompanyViewSet
from clients.views import ClientViewSet
from applications.views import ApplicationViewSet
from servers.views import ServerViewSet
from clientapplications.views import ClientApplicationViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'applications', ApplicationViewSet)
router.register(r'servers', ServerViewSet)
router.register(r'companies', CompanyViewSet)
router.register(r'clients', ClientViewSet)
router.register(r'clientapplications', ClientApplicationViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djmicrosip_manager.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
)
