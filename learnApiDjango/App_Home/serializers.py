from rest_framework import serializers
from .models import App_Home_DB


class GetAllData(serializers.ModelSerializer):
  
  class Meta:
    model = App_Home_DB
    fields = ('id', 'name', 'email', 'phoneNumber')