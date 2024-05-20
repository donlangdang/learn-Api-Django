from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import App_Home_DB, Profile
from .serializers import GetAllData, GetAllProfile, PostAllProfile

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
  https://docs.djangoproject.com/en/5.0/topics/db/queries/
"""

class GetAllDataAPI(APIView):
  # ở đây là quyền xác thực người dùng xem ai đăng nhập, ai có quyền dùng api...
  permission_classes=[IsAuthenticated]
  
  def get(self, request):
    if request.method == 'GET':
      list_AllData = App_Home_DB.objects.all()
      mydata = GetAllData(list_AllData, many=True)
      if mydata:
        return Response(data=mydata.data, status=status.HTTP_200_OK)
      return Response(mydata.errors, status=status.HTTP_400_BAD_REQUEST)
  def post(self, request):
    if request.method == 'POST':
      dataPost = GetAllData(data=request.data)
      if dataPost.is_valid():
        dataPost.save()
        return Response(dataPost.data, status=status.HTTP_201_CREATED)
      return Response(dataPost.errors, status=status.HTTP_400_BAD_REQUEST)
    
class GetAllDataProfile(APIView):
  permission_classes=[IsAuthenticated]
  
  def get(self, request):
    if request.method == 'GET':
      list_AllDataProfile = Profile.objects.all()
      myDataProfile = GetAllProfile(list_AllDataProfile, many=True)
      if myDataProfile:
        return Response(myDataProfile.data, status=status.HTTP_200_OK)
      return Response(myDataProfile.errors, status=status.HTTP_400_BAD_REQUEST)
  def post(self, request):
    if request.method =='POST':
      dataPostProfile = PostAllProfile(data=request.data)
      if dataPostProfile.is_valid():
        dataPostProfile.save()
        return Response(dataPostProfile.data, status=status.HTTP_201_CREATED)
      return Response(dataPostProfile.errors, status=status.HTTP_400_BAD_REQUEST)