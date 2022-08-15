from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import main_data

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = ('username','password')

class MainData(serializers.ModelSerializer):
    class Meta:
        model = main_data
        fields = '__all__'