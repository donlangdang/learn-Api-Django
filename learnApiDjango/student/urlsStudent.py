from django.urls import path, re_path
from .views import StudentAPI, SubjectAPI, StudentSubjectAPI, GetPutStudentById, GetPutSuvjectAPI


urlpatterns = [
  path('', StudentAPI.as_view()),
  path('subject/', SubjectAPI.as_view()),
  path('student-subject/', StudentSubjectAPI.as_view()),
  path('<int:pk>/', GetPutStudentById.as_view()),
  path('subject/<int:pk>/', GetPutSuvjectAPI.as_view())
]