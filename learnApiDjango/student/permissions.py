from rest_framework import permissions
# from django.contrib.auth import get_user_model
# from .models import Student
'''
ở đây để phân quyền cho ai có thể truy cập vào api rồi import vào view
trong view trong class nào muốn có permissions thì
khai báo permission_classes = [IsAuthenticated, IsUserWithIdOne]
'''
# UserId = get_user_model()

class PermissionsForUserId(permissions.BasePermission):
  def has_permission(self, request, view):
    
    user_id = view.kwargs.get('pk')
    return request.user.is_authenticated and request.user.id == int(user_id)
# Thuộc tính Chính của request
  # https://www.django-rest-framework.org/api-guide/requests/#request-parsing


#   Thuộc tính Chính của View:
# request:
  # Mô tả: Đối tượng HttpRequest hiện tại, chứa tất cả thông tin về yêu cầu HTTP.
  # Ví dụ: view.request.method để lấy phương thức HTTP của yêu cầu.
  
# kwargs:
  # Mô tả: Từ điển chứa các tham số URL bắt buộc (keyword arguments).
  # Ví dụ: view.kwargs.get('pk') để lấy giá trị của tham số pk từ URL.
  
# args:
  # Mô tả: Danh sách các tham số URL không bắt buộc (positional arguments).
  # Ví dụ: view.args để truy cập các tham số vị trí trong URL.
  
# action:
  # Mô tả: Tên của hành động hiện tại, chỉ có sẵn trong viewset.
  # Ví dụ: view.action có thể trả về các giá trị như 'list', 'retrieve', 'create', v.v.
  
# basename:
  # Mô tả: Tên cơ sở của route, chỉ có sẵn trong viewset.
  # Ví dụ: view.basename có thể trả về tên cơ sở như 'user'.
  
# queryset:
  # Mô tả: Queryset mặc định cho view, dùng để truy xuất dữ liệu từ cơ sở dữ liệu.
  # Ví dụ: view.queryset để truy cập vào queryset được định nghĩa trong view.
  
# serializer_class:
  # Mô tả: Lớp serializer được sử dụng để xác định và xác thực dữ liệu.
  # Ví dụ: view.serializer_class để truy cập vào lớp serializer được định nghĩa trong view.
