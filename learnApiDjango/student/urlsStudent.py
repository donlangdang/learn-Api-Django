from django.urls import path, re_path
from .views import StudentAPI, SubjectAPI, StudentSubjectAPI, GetPutStudentById, GetPutSuvjectAPI, UserRegisterView
from rest_framework_simplejwt.views import (
  TokenObtainPairView,
  TokenRefreshView
)

"""
  TokenObtainPairView để lấy access và refresh token
   - access dùng để xác thực và cho người dùng truy cập vào api
   Authorization Bearer access
   - refresh dùng để refresh lại access token mới khi access token cũ đã hết hạn refresh token có thời hạn lâu hơn access token nhiều
   - cái này dùng phương thức post username(email) và password sẽ trả về access và refresh rồi dùng access để làm xác thực
  TokenRefreshView: dùng post với keyword là:
  "refresh": "access token hết hạn" để cấp access token mới
"""


urlpatterns = [
  path('', StudentAPI.as_view()),
  path('subject/', SubjectAPI.as_view()),
  path('student-subject/', StudentSubjectAPI.as_view()),
  path('<int:pk>/', GetPutStudentById.as_view()),
  path('subject/<int:pk>/', GetPutSuvjectAPI.as_view()),
  path('register/', UserRegisterView.as_view()),
  path('token/', TokenObtainPairView.as_view()),
  path('token/refresh/', TokenRefreshView.as_view())
]