from django.conf.urls import patterns, include, url
from django.contrib import admin
from servers.models import Server
from clientapplications.models import ClientApplication
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


# Serializers define the API representation.
class ClientSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Client
        fields = ('user',)

# ViewSets define the view behavior.
class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

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
    client = ClientSerializer()

    class Meta:
        model = ClientApplication
        fields = ('application','version','client',)

# ViewSets define the view behavior.
class ClientApplicationViewSet(viewsets.ModelViewSet):
    queryset = ClientApplication.objects.all()
    serializer_class = ClientApplicationSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        client_id = self.kwargs['pk']
        return ClientApplication.objects.filter(client__id=client_id)

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
