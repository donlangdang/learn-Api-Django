from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import App_Home_DB
from .serializers import GetAllData

# Create your views here.
# giống controller
# để có api có tất cả các phương thức GET, POST, PUT, DELETE, UPDATE thì dùng:
# from rest_framework import viewsets
# viewsets.ModelViewSet
# viewsets không phải class con của APIView
"""
  ở đây có APIView là class cha của các class view khác ở đây quy định các phương thức được phép dùng hoặc có thể dùng tất cả các phương thức.
  có các class con chỉ quy định 1 hay nhiều phương thức nhất định
  
  models.object.(...) dùng để truy vấn các dữ liệu từ database hoặc cũng có thể sửa trong database
"""

class GetAllDataAPI(APIView):
  permission_classes=[IsAuthenticated]
  
  def get(self, request):
    if request.method == 'GET':
      list_AllData = App_Home_DB.objects.all()
      mydata = GetAllData(list_AllData, many=True)
      return Response(data=mydata.data, status=status.HTTP_200_OK)
  def post(self, request):
    if request.method == 'POST':
      dataPost = GetAllData(data=request.data)
      if dataPost.is_valid():
        dataPost.save()
        return Response(dataPost.data, status=status.HTTP_201_CREATED)
      return Response(dataPost.errors, status=status.HTTP_400_BAD_REQUEST)