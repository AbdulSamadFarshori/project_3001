from django.urls import path
from .views import HomeView, LoginView, MainView, CompletedCasesPageTemplate

urlpatterns = [
    path('', HomeView.as_view()),
    path('login', LoginView.as_view(), name="login"),
    path('main/<var>', MainView.as_view(), name="main"),
    path('completed-cases', CompletedCasesPageTemplate.as_view(), name="completed"),
    ]