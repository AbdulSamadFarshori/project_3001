from django.urls import path
from .views import (  
							IntentApiView, 
							RegisterApiView, 
							SymptomsApiView, 
							LinkConfigApiView,
							PatientAskingApiView,
							HistoryApiView,
							EffectApiView,
							MarkAsCompletedApiView,
							MarkAsInCompletedApiView,
							CauseApiView
							)

from .models import main_data
from api.serializers import MainData
from rest_framework_simplejwt.views import (
    										TokenObtainPairView,
    										TokenRefreshView,
											)
urlpatterns = [
		path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    	path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    	path('intent', IntentApiView.as_view(), name='intent' ),
    	path('user-register', RegisterApiView.as_view(), name='user_register' ),
    	path("symptoms", SymptomsApiView.as_view(), name="symptoms"),
    	path("links", LinkConfigApiView.as_view(), name="link_api"),
    	path("patient-asking", PatientAskingApiView.as_view(), name="patient-asking"),
    	path("history", HistoryApiView.as_view(), name="history"),
    	path("effect", EffectApiView.as_view(), name="effect"),
    	path("mark-completed", MarkAsCompletedApiView.as_view(), name="mark-completed"),
    	path("mark-incompleted", MarkAsInCompletedApiView.as_view(), name="mark-incompleted"),
    	path("cause", CauseApiView.as_view(), name="cause"),

		]