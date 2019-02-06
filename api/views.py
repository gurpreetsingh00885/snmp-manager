from snmp_manager.users.models import User
from rest_framework import viewsets
from rest_framework import views
from api.serializers import UserSerializer
from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class Home(views.APIView):
    """
    Sample api view
    """
    def get(self, request, format=None):
        return Response({"status": "OK"})

home = Home.as_view()
