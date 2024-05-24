from rest_framework import serializers
from .models import Student, Subject, Student_Subject, CustomUsers


class GetAllStudent(serializers.ModelSerializer):
  
  class Meta:
    model = Student
    fields = ('id', 'name', 'birthDate', 'className', 'subject')
    depth = 1
    # trường này dùng để khai báo, bổ sung thêm thông tin khi truy vấn..
    # extra_kwargs = {'name': {'write_only': True}}
    
class GetAllSubject(serializers.ModelSerializer):
  
  class Meta:
    model = Subject
    fields = ('id', 'name', 'createdDate', 'updateDate', 'students')
    depth = 1
    
class GetStudent_Subject(serializers.ModelSerializer):
  
  # studentInfo = GetAllStudent()
  # subject = GetAllSubject
  
  class Meta:
    model = Student_Subject
    fields = ('studentInfo', 'subject')
    depth = 1
    
class PostStudent_Subject(serializers.ModelSerializer):
  
  class Meta(GetStudent_Subject.Meta):
    depth = 0
    
class UserSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = CustomUsers
    fields = ('email', 'password')
    extra_kwargs = {'password': {'write_only': True}}