from django.shortcuts import render
from django.views import View
from .models import Company
from django.http import JsonResponse
# Create your views here.
class CompanyView(View):
    def get(self, request):
        listReserv = Company.objects.all()
        return JsonResponse(list(listReserv.values()), safe=False)

        
    