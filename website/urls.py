from django.urls import path
from .views import HomeView, LoginView, MainView

urlpatterns = [
    path('', HomeView.as_view()),
    path('login', LoginView.as_view(), name="login"),
    path('main/<var>', MainView.as_view(), name="main")
    ]