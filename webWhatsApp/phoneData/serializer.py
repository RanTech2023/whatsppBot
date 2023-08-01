from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from phoneData.models import PhoneData  
class PhoneDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneData
        fields = '__all__'