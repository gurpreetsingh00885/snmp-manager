import re
from snmp_manager.users.models import User
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import views
from api.models import Host, HostParameter
from api.serializers import UserSerializer, HostSerializer
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

class CreateOrUpdateHostView(views.APIView):
    """
    To be called only by our traphandler script in order to update or add
    information about a certain host.
    """
    def post(self, request, format=None):
        ip = request.data['ip']
        ip_addr = re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", ip)[0]
        variables = request.data["vars"]
        temp = {}
        for oid, val in [x.split("<is>") for x in variables.split(',')]:
            temp[oid] =  val
        temp.pop("SNMPv2-MIB::snmpTrapOID.0")
        mac_addr = temp.pop("IF-MIB::ifPhysAddress")
        host, created = Host.objects.get_or_create(mac_addr=mac_addr, current_ip=ip_addr)

        if created:
            for oid in temp:
                HostParameter.objects.create(oid=oid,
                                             value=temp[oid],
                                             host=host)
        else:
            for oid in temp:
                param = HostParameter.objects.get(oid=oid, host=host)
                param.value = temp[oid]
                param.save()

        return Response({"status" : "successful"})

create_update_host = CreateOrUpdateHostView.as_view()

class HostListView(generics.ListAPIView):
    model = Host
    queryset = Host.objects.all()
    serializer_class = HostSerializer

host_list = HostListView.as_view()
