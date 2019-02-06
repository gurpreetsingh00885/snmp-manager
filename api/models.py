from django.db import models

class Host(models.Model):
    """
    Any entity on a network capable of SNMP
    """
    mac_addr = models.CharField(max_length=100, null=True, blank=False)
    current_ip = models.CharField(max_length=15, null=True, blank=False)

    def __str__(self):
        return self.mac_addr


class HostParameter(models.Model):
    """
    Model to store individual parameters i.e. info about a particular host.
    """
    host = models.ForeignKey(Host, related_name='parameters', on_delete=models.CASCADE)
    oid = models.CharField(max_length=100, null=True, blank=True)
    value = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.host.mac_addr + "(" + self.oid + ")"
