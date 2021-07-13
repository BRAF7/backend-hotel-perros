from django.shortcuts import render
from django.views import View
from .models import Company
from django.http import JsonResponse
from rest_framework import viewsets
from .serializers import CompanySerializer

# Create your views here.
class CompanyView( viewsets.ModelViewSet):
    queryset = Company.objects.all().order_by('date')
    serializer_class = CompanySerializer
    

        
    