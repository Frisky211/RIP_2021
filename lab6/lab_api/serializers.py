from lab_api.models import Phone, Manufacturer
from rest_framework import serializers

class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = ['idphone', 'model', 'description', 'diag', 'capacity', 'manufacturer']
        depth = 1

class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ['idmanufacturer', 'name', 'country']
