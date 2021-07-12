from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'company', views.CompanyView)

urlpatterns = [path('', include(router.urls)),
               path('company/', include('rest_framework.urls'), name= 'rest_framework')]
