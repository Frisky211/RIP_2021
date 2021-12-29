from rest_framework import viewsets
from lab_api.serializers import PhoneSerializer, ManufacturerSerializer
from lab_api.models import Phone, Manufacturer

class PhoneViewSet(viewsets.ModelViewSet):
    queryset = Phone.objects.all().order_by('idphone')
    serializer_class = PhoneSerializer

class ManufacturerViewSet(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all().order_by('name')
    serializer_class = ManufacturerSerializer
