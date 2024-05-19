from django.db import models

# Create your models here.
# ở đây sẽ khai báo các trường(column) trong bảng App_Home_DB
# xem các field tại đây: https://docs.djangoproject.com/en/5.0/ref/models/fields/
# sau khi khai báo các bảng xong có đầy đủ các thông tin

# say khi khai báo xong field thì chạy lệnh:
# python manage.py makemigrations tên_app(ở đây là App_Home)
# lệnh này sẽ tạo file 0001_initial.py file này sẽ ghi rõ sẽ tạo bảng gì field gì
# tiếp theo chạy lệnh python manage.py migrate
# lệnh này sẽ tạo bảng bảng và cột luôn tên bảng mặc định là: 
# tên_app_tên_model trong trường hợp này là: App_Home_app_home_db
# ngoài ra trong này có class con là class Meta dùng định nghĩa hoặc cài đặt 1 số thứ liên quan
# https://docs.djangoproject.com/en/5.0/ref/models/options/
class App_Home_DB(models.Model):
  name = models.CharField(max_length=255)
  email = models.EmailField(max_length=255)
  phoneNumber = models.IntegerField()
  
  def __str__(self):
    return self.name
  
class Profile(models.Model):
  birthday = models.CharField(max_length=10)
  school = models.CharField(max_length=255, blank=True)
  work = models.CharField(max_length=255, blank=True)
  married = models.BooleanField()
  people = models.OneToOneField(
    App_Home_DB,
    on_delete=models.CASCADE,
    related_name='profile'
  )
  
  def __str__(self):
        return self.birthday
