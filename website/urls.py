from django.urls import path
from .views import (
                    HomeView, 
                    LoginView, 
                    MainView, 
                    CompletedCasesPageTemplate, 
                    NotCompletedCasesPageTemplate,
                    IntentCasesPageTemplate,
                    UpdateIntentCasesTemplate,
                    EntityCasesPageTemplate,
                    UpdateEntityCasesTemplate
                    )

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('login', LoginView.as_view(), name="login"),
    path('main/<var>', MainView.as_view(), name="main"),
    path('completed-cases', CompletedCasesPageTemplate.as_view(), name="completed"),
    path('not-completed-cases', NotCompletedCasesPageTemplate.as_view(), name="not-completed"),
    path('add-intent/<pk>', IntentCasesPageTemplate.as_view(), name="add-intent"),
    path('update-intent/<pk>', UpdateIntentCasesTemplate.as_view(), name="update-intent"),
    path('add-symptoms/<pk>', EntityCasesPageTemplate.as_view(), name="symptoms"),
    path('update-symptoms/<pk>', UpdateEntityCasesTemplate.as_view(), name="update-symptoms"),
    ]