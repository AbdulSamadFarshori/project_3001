from django.urls import path
from .views import HomeView, LoginView

urlpatterns = [
    path('', HomeView.as_view()),
    path('login', LoginView.as_view())
    ]