from rest_framework import serializers
from .models import App_Home_DB, Profile


"""
serializers sẽ lấy các trường trong object rồi chuyển các trường này qua dạng json
cần kế thừa như trong đoạn code này rồi viết ra các fields cần lấy ra của 1 object nào đó trong trường hợp này là lấy object của models
sau đó lấy class vừa được tạo ở đây gắn tham số là 1 object cần chuyển sang json
vd ở đầy là GetAllData(App_Home_DB) rồi .data thì sẽ được chuyển sang json
GetAllData(App_Home_DB).data => sẽ trả về dạng json

ModelSerializer 
https://www.django-rest-framework.org/api-guide/serializers/#modelserializer

muốn lấy dữ liệu từ db ra json mà lồng nhau thì dùng: PrimaryKeyRelatedField
https://www.django-rest-framework.org/api-guide/relations/

các class được định nghĩa ở đây cho phép chỉ sửa trên cơ sở dữ liệu hoặc không.
có những class chỉ được đọc có những class làm nhiệm vụ khác.
"""

class GetAllProfile(serializers.ModelSerializer):
  
  
  class Meta:
    model = Profile
    fields = ('__all__')
    depth = 1
    
# ở đây phương thức post nếu dùng depth = 1 thì không được vì serializers chỉ trả về json mà post thì cũng đi từ json đó qua serializers sẽ ko post được nó sẽ để null
# phải để depth = 0 chỉ lấy bảng đó ra rồi mới post với people là số được.
class PostAllProfile(serializers.ModelSerializer):
  class Meta(GetAllProfile.Meta):
    depth = 0
    

class GetAllData(serializers.ModelSerializer):
  
  
  class Meta:
    model = App_Home_DB
    fields = ('id', 'name', 'email', 'phoneNumber', 'profile')
    depth = 1
    
    
    