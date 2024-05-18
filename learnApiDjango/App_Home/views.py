from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import App_Home_DB
from .serializers import GetAllData

# Create your views here.

class GetAllDataAPI(APIView):
  
  def get(self, request):
    list_AllData = App_Home_DB.objects.all()
    mydata = GetAllData(list_AllData, many=True)
    return Response(data=mydata.data, status=status.HTTP_200_OK)