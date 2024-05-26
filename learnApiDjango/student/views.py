from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Response(data, status=None, template_name=None, headers=None, content_type=None)
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Student, Subject, Student_Subject
from .serializers import (
  GetAllStudent,
  GetAllSubject,
  GetStudent_Subject,
  PostStudent_Subject,
  UserSerializer)

# đoạn import này để hash password.
from django.contrib.auth.hashers import make_password
# cái này là để lấy model user mặc định ra
# vì ta đã khai báo user custom làm user mặc định
# nên ở đây sẽ là user custom
from django.contrib.auth import get_user_model
# IsUserWithIdOne để cấp quyền cho ai đó có id hoặc username...
# khai báo như thế này trong mỗi class cần được cấp quyền truy cập
# permission_classes = [IsAuthenticated, IsUserWithIdOne]
from .permissions import PermissionsForUserId
from django.contrib.auth import authenticate
# Create your views here.

# api lấy tất cả student hoặc post student
class StudentAPI(APIView):
  # permission_classes = [IsAuthenticated]
  
  def get(self, request):
    if request.method == 'GET':
      lisAllStudent = Student.objects.all()
      myStudentData = GetAllStudent(lisAllStudent, many=True)
      if not myStudentData:
        return Response(myStudentData.errors, status=status.HTTP_400_BAD_REQUEST)
      return Response(myStudentData.data, status=status.HTTP_200_OK)
    
  def post(self, request):
    if request.method == 'POST':
      dataStudentPost = GetAllStudent(data=request.data)
      if dataStudentPost.is_valid():
        dataStudentPost.save()
        return Response(dataStudentPost.data, status=status.HTTP_201_CREATED)
      return Response(dataStudentPost.errors, status=status.HTTP_400_BAD_REQUEST)

# class để lấy student theo id bằng pk(primary key) và để cập nhật thông tin student
class GetPutStudentById(APIView):
  
  permission_classes = [IsAuthenticated, PermissionsForUserId]
  
  def get(self, request, pk):
    if request.method == 'GET':
      try:
        studentById = Student.objects.get(pk=pk)
      except:
        return Response(
          {"messeage": "this person does not exists or delete"},
          status=status.HTTP_400_BAD_REQUEST
          )
      studentData = GetAllStudent(studentById)
      if not studentData:
        return Response(studentData.errors, status=status.HTTP_400_BAD_REQUEST)
      return Response(studentData.data, status=status.HTTP_200_OK)   
  def put(self, request, pk):
    if request.method == 'PUT':
      try:
        studentId = Student.objects.get(pk=pk)
      except:
        return Response(
          {"messeage": "this person does not exists or delete"},
          status=status.HTTP_400_BAD_REQUEST
        )
      
      dataPut = request.data
      mergeData = GetAllStudent(studentId).data
      for keyMergeData in mergeData:
        for keyDataPut in dataPut:
          if keyMergeData == keyDataPut:
            mergeData[keyMergeData] = dataPut.get(keyDataPut)
      
      myPutData = GetAllStudent(studentId, data=mergeData)
      if myPutData.is_valid():
        myPutData.save()
        return Response(myPutData.data, status=status.HTTP_201_CREATED)
      return Response(myPutData.errors, status=status.HTTP_400_BAD_REQUEST)
          

# api để lấy tất cả thông tin subject trong db và post subject mới vào db
class SubjectAPI(APIView):
  # permission_classes = [IsAuthenticated]
  
  def get(self, request):
    if request.method == 'GET':
      listAllSubject = Subject.objects.all()
      mySubjectData = GetAllSubject(listAllSubject, many=True)
      if not mySubjectData:
        return Response(mySubjectData.errors, status=status.HTTP_400_BAD_REQUEST)
      return Response(mySubjectData.data, status=status.HTTP_200_OK)
  
  def post(self, request):
    if request.method == 'POST':
      dataSubjectPost = GetAllSubject(data=request.data)
      if dataSubjectPost.is_valid():
        dataSubjectPost.save()
        return Response(dataSubjectPost.data, status=status.HTTP_201_CREATED)
      return Response(dataSubjectPost.errors, status=status.HTTP_400_BAD_REQUEST)

# lấy các subject theo id hoặc cập nhật subject đã có sẵn
class GetPutSuvjectAPI(APIView):
  
  def get(self, request, pk):
    if request.method == 'GET':
      try:
        subjectId = Subject.objects.get(pk=pk)
      except:
        return Response(
          {"messeage": "this person does not exists or delete"},
          status=status.HTTP_400_BAD_REQUEST
        )
      mySubjectIdData = GetAllSubject(subjectId)
      if not mySubjectIdData:
        return Response(status=status.HTTP_400_BAD_REQUEST)
      return Response(mySubjectIdData.data, status=status.HTTP_200_OK)
    
  def put(self, request, pk):
    if request.method == 'PUT':
      try:
        subjectId = Subject.objects.get(pk=pk)
      except:
        return Response(
          {"messeage": "this person does not exists or delete"},
          status=status.HTTP_400_BAD_REQUEST
        )
      myputData = GetAllSubject(subjectId, data=request.data)
      if myputData.is_valid():
        myputData.save()
        return Response(myputData.data, status=status.HTTP_201_CREATED)
      return Response(myputData.errors, status=status.HTTP_400_BAD_REQUEST)

# lấy thông tin về student có các subject nào hoặc thêm mới subject vào thông tin student
class StudentSubjectAPI(APIView):
  # permission_classes = [IsAuthenticated]
  
  def get(self, request):
    if request.method == 'GET':
      dataStudentSubject = Student_Subject.objects.all()
      myStudentSubjectData = GetStudent_Subject(dataStudentSubject, many=True)
      if not myStudentSubjectData:
        return Response(myStudentSubjectData.errors, status=status.HTTP_400_BAD_REQUEST)
      return Response(myStudentSubjectData.data, status=status.HTTP_200_OK)
  
  def post(self, request):
    if request.method == 'POST':
      dataStudentSubjectPost = PostStudent_Subject(data=request.data)
      if dataStudentSubjectPost.is_valid():
        dataStudentSubjectPost.save()
        return Response(dataStudentSubjectPost.data, status=status.HTTP_201_CREATED)
      return Response(dataStudentSubjectPost.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
# đăng kí user với user đã được custom trong models
class UserRegisterView(APIView):
  def post(self, request):
    postEmail_Password = UserSerializer(data=request.data)
    if postEmail_Password.is_valid():
      postEmail_Password.validated_data['password'] = make_password(postEmail_Password.validated_data['password'])
      postEmail_Password.save()
      return Response({ "message": "register successful!"}, status=status.HTTP_201_CREATED)
    return Response({
      "error_message": "This email has already exist!",
      "errors_code": 400,
    }, status=status.HTTP_400_BAD_REQUEST)
    
    
# đăng nhập user:
class UserLoginView(APIView):
  def post(self, request):
    username = request.data['email']
    password = request.data['password']
    # authenticate() để xác thực thông tin người dùng
    # class này còn phải sửa nữa
    user = authenticate(username=username, password=password)
    if user is not None:
      return Response({'mess': "You are logged in"}, status=status.HTTP_200_OK)
    return Response({'mess': "Invalid login"}, status=status.HTTP_400_BAD_REQUEST)
  
# thay đổi email hoặc mật khẩu cho user
class ChangePassword(APIView):
  
  def put(self, request):
    email = request.data['email']
    oldPassword = request.data['oldPassword']
    newPassword = request.data['newPassword']
    confirmPassword = request.data['confirmPassword']
    user = authenticate(username=email, password=oldPassword)
    if user is not None:
      if newPassword == confirmPassword:
        User = get_user_model()
        userChangePassword = User.objects.get(email=email)
        userChangePassword.set_password(confirmPassword)
        userChangePassword.save()
        return Response({'mess': "đổi mật khẩu thành công"}, status=status.HTTP_201_CREATED)
      return Response({'mess': 'xác nhận mật khẩu sai'}, status=status.HTTP_400_BAD_REQUEST)
    return Response({'mess': 'user chưa đăng kí hoặc không có'}, status=status.HTTP_400_BAD_REQUEST)
        
# custom payload trong jwt(json wed token)

# cái này để xử lí sau làm thành thạo các bước trên đã...
# Oh NOOOOO! cái này nhiều trường hợp quá thôi để từ từ đã phải ổn mấy cái ở trên đã
# cái này là bảo mật và an toàn thông tin rồi nên từ từ đã....

# xử lí 2+ người cùng dùng chung 1 access token đã hết hạn để lấy access token mới
# vd 1 người dùng access token hết hạn để lấy token mới để đăng nhập thì được ko sao cả
# chuyện xảy ra khi có người thứ 2 hoặc nhiều hơn dùng token hết hạn để lấy token mới
# - Cả RT và AT đều cùng được cấp mới mỗi lần tạo mới AT, và lưu lại RT cũ.
# - Một khi RT cũ bị sử dụng lại (không cần phân biệt user hay hacker) thì hủy toàn bộ RT đang hoạt động.
# - User đăng nhập lại và lấy RT mới.