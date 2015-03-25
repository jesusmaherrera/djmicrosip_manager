from django.conf.urls import patterns, include, url
from django.contrib import admin
from servers.models import Server
from clientapplications.models import ClientApplication
from applications.models import Application
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class ApplicationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Application
        fields = ('name','description',)

# ViewSets define the view behavior.
class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

# Serializers define the API representation.
class ClientApplicationSerializer(serializers.HyperlinkedModelSerializer):
    application = ApplicationSerializer()
    
    class Meta:
        model = ClientApplication
        fields = ('application','version',)

# ViewSets define the view behavior.
class ClientApplicationViewSet(viewsets.ModelViewSet):
    queryset = ClientApplication.objects.all()
    serializer_class = ClientApplicationSerializer

class ServerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Server
        fields = ('name', 'user_name', 'mac_address')

# ViewSets define the view behavior.
class ServerViewSet(viewsets.ModelViewSet):
    queryset = Server.objects.all()
    serializer_class = ServerSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'applications', ApplicationViewSet)
router.register(r'servers', ServerViewSet)
router.register(r'clientapplications', ClientApplicationViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djmicrosip_manager.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
)
