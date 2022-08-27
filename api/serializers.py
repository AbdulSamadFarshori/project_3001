from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import main_data, ReplyData, ReplyThread, LinkConfig
from website.models import Cookies

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = ('username','password')

class MainData(serializers.ModelSerializer):
    class Meta:
        model = main_data
        fields = '__all__'

class ReplyDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReplyData
        fields = '__all__'

class ReplyThreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReplyThread
        fields = '__all__'

class LinkConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = LinkConfig
        fields = '__all__'

class CookiesSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Cookies
        fields = ('set_cookies')


