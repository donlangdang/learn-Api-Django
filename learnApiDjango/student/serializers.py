from rest_framework import serializers
from .models import Student, Subject, Student_Subject


class GetAllStudent(serializers.ModelSerializer):
  
  class Meta:
    model = Student
    fields = ('id', 'name', 'birthDate', 'className', 'subject')
    depth = 1
    
class GetAllSubject(serializers.ModelSerializer):
  
  class Meta:
    model = Subject
    fields = ('id', 'name', 'createdDate', 'updateDate', 'students')
    depth = 1
    
class GetStudent_Subject(serializers.ModelSerializer):
  
  class Meta:
    model = Student_Subject
    fields = ('__all__')
    depth = 1
    
class PostStudent_Subject(serializers.ModelSerializer):
  
  class Meta(GetStudent_Subject.Meta):
    depth = 0