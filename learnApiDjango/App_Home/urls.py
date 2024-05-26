from django.urls import path, re_path
from .views import GetAllDataAPI, GetAllDataProfile, GetPutDataById


urlpatterns = [
  path('', GetAllDataAPI.as_view()),
  path('profile/', GetAllDataProfile.as_view()),
  path('<int:pk>/', GetPutDataById.as_view())
]