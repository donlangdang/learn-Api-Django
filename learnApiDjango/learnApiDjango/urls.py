"""
URL configuration for learnApiDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
# from App_Home.views import GetAllDataAPI, GetAllDataProfile

# biểu thức chính quy để làm url thì dùng re_path chứ ko dùng path
urlpatterns = [
    path('apphome/', include('App_Home.urls')),
    path('student/', include('student.urls')),
    path('admin/', admin.site.urls),
    # path('apphome/', GetAllDataAPI.as_view()),
    # path('profile/', GetAllDataProfile.as_view())
]
