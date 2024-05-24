from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime

# Create your models here.
# nếu làm user mới kế thừa từ user của django thì làm như này 
# và qua setting.py sửa lại 
# AUTH_USER_MODEL = 'student.User'

# AbstractUser : Sử dụng option này nếu như bạn muốn sử dụng các trường sẵn có    
# của User và chỉ muốn remove trường username.
# AbstractBaseUser: Sử dụng option này nếu như bạn muốn tạo mới hoàn toàn một 
# User model mới.

class CustomUsers(AbstractUser):
  username = None
  last_login = None
  is_staff = None
  is_superuser = None
  
  password = models.CharField(max_length=100)
  # unique=True là email là độc nhất không trùng với các row khác
  email = models.EmailField(max_length=100, unique=True)
  
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = []
  
  def __str__(self):
    return self.email
  

class Student(models.Model):
  name = models.CharField(max_length=100)
  birthDate = models.DateField()
  className = models.CharField(max_length=255)
  
class Subject(models.Model):
  name = models.CharField(max_length=100)
  createdDate = models.DateField(default=datetime.date.today)
  updateDate = models.DateField(auto_now=True)
  
  class Meta:
    unique_together = ['name']
  
class Student_Subject(models.Model):
  studentInfo = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='subject')
  subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="students")
  
  class Meta:
    """
    cái này dùng để làm class cha để các model con kế thừa khi dùng chung nhiều field
    khi khai báo cái này thì model đó sẽ ko được tạo trong database mà để các class con kế thừa 
    abstract = True
    """
    unique_together = ('studentInfo', 'subject')