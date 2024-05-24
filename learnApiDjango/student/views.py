from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Student, Subject, Student_Subject
from .serializers import GetAllStudent, GetAllSubject, GetStudent_Subject, PostStudent_Subject, UserSerializer
# đoạn import này để hash password.
from django.contrib.auth.hashers import make_password
# from .permissions import IsUserWithIdOne
# Create your views here.

class StudentAPI(APIView):
  permission_classes = [IsAuthenticated]
  
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
    
class GetPutStudentById(APIView):
  
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
    
    
# đăng kí user
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