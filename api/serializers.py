from api.models import Host, HostParameter
from snmp_manager.users.models import User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email')


class HostParameterSerializer(serializers.ModelSerializer):
    class Meta:
        model = HostParameter
        fields = ('oid', 'value')


class HostSerializer(serializers.ModelSerializer):
    parameters = HostParameterSerializer(many=True, read_only=True)

    class Meta:
        model = Host
        fields = ('mac_addr', 'current_ip', 'parameters')
