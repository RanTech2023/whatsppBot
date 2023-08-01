from django.shortcuts import render
from rest_framework import viewsets
from phoneData.models import PhoneData
from phoneData.serializer import PhoneDataSerializer
class PhoneDataViewSet (viewsets.ModelViewSet):
    queryset = PhoneData.objects.all()
    serializer_class = PhoneDataSerializer
# Create your views here.
