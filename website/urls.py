from django.urls import path
from .views import HomeView, LoginView, MainView, LabelView

urlpatterns = [
    path('', HomeView.as_view()),
    path('login', LoginView.as_view(), name="login"),
    path('main/<var>', MainView.as_view(), name="main"),
    path('label/value', LabelView.as_view(), name="main")
    ]