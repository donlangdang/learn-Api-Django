from django.urls import path, re_path
from .views import GetAllDataAPI, GetAllDataProfile


urlpatterns = [
  path('apphome/', GetAllDataAPI.as_view()),
  path('profile/', GetAllDataProfile.as_view())
]