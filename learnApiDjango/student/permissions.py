from rest_framework.permissions import BasePermission

'''
ở đây để phân quyền cho ai có thể truy cập vào api rồi import vào view
trong view trong class nào muốn có permissions thì
khai báo permission_classes = [IsAuthenticated, IsUserWithIdOne]
'''

class IsUserWithIdOne(BasePermission):
  def has_permission(self, request, view):
    return request.user and request.user.id == 1