from django.urls import path
from .views import ( 
							LoginView, 
							FormSubmitView, 
							RegisterApiView, 
							MainDataApiView, 
							ReplyDataApiView,
							ReplyThreadApiView,
							LinkConfigApiView,
							LabelApiView)

from .models import main_data
from api.serializers import MainData
from rest_framework_simplejwt.views import (
    										TokenObtainPairView,
    										TokenRefreshView,
											)
urlpatterns = [
		path("login", LoginView.as_view(), name="login_api"),
		path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    	path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    	path('submit', FormSubmitView.as_view(), name='form_submit' ),
    	path('user-register', RegisterApiView.as_view(), name='user_register' ),
    	path("main-data", MainDataApiView.as_view(), name="main_data_api"),
    	path("reply-data", ReplyDataApiView.as_view(), name="reply_data_api"),
    	path("reply-thread", ReplyThreadApiView.as_view(), name="reply_thread_api"),
    	path("links", LinkConfigApiView.as_view(), name="link_api"),
    	path("label", LabelApiView.as_view(), name="label")
		]