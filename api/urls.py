from django.urls import path
from .views import GetDataFromBitIo, LoginView
from .models import main_data
from api.serializers import MainData
from rest_framework_simplejwt.views import (
    										TokenObtainPairView,
    										TokenRefreshView,
											)
urlpatterns = [
		path("get-cases", GetDataFromBitIo.as_view(), name="get_cases"),
		path("login", LoginView.as_view(), name="login_api"),
		path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    	path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
		]