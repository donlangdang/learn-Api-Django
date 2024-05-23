from django.db import models
import datetime

# Create your models here.
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