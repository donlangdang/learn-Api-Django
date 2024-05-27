from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import Token
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
    
"""
custom payload trong JWT thì làm 1 serializer để có thể truy cập vào model và xác thực.
rồi sang views.py làm custom view kế thừa từ class TokenObtainPairView
rồi khai báo serializer_class = CustomTokenSerializers để view giao tiếp với serializer.
ở đây lấy về payload jwt có email thì khai báo như dưới
"""
class CustomTokenSerializers(TokenObtainPairSerializer):
  @classmethod
  def get_token(cls, user):
    token = super().get_token(user)
    
    token['email'] = user.email
    
    return token
  
  """
  Phương thức super() trong Python được sử dụng để gọi các phương thức từ lớp cha (superclass) của một lớp con (subclass). Điều này hữu ích trong các tình huống kế thừa, khi bạn muốn mở rộng hoặc thay đổi hành vi của phương thức trong lớp con mà vẫn duy trì một phần hoặc toàn bộ chức năng từ lớp cha.
  """