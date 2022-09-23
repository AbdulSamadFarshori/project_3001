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
                    UpdateEntityCasesTemplate, 
                    CauseCasesPageTemplate,
                    UpdatdeCauseTempalte,
                    PatientAskingForPageTemplate,
                    UpdatePatientAskingForTemplate,
                    HistoryPageTemplate,
                    UpdateHistoryTemplate,
                    EffectPageTemplate,
                    UpdateEffectTemplate
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
    path('add-cause/<pk>', CauseCasesPageTemplate.as_view(), name="add-cause"),
    path('update-cause/<pk>', UpdatdeCauseTempalte.as_view(), name="update-cause"),
    path('add-patient-asking-for/<pk>', PatientAskingForPageTemplate.as_view(), name="add-patient-asking-for"),
    path('update-patient-asking-for/<pk>', UpdatePatientAskingForTemplate.as_view(), name="update-patient-asking-for"),
    path('add-history/<pk>', PatientAskingForPageTemplate.as_view(), name="add-history"),
    path('update-history/<pk>', UpdatePatientAskingForTemplate.as_view(), name="update-history"),
    path('add-effect/<pk>', EffectPageTemplate.as_view(), name="add-effect"),
    path('update-effect/<pk>', UpdateEffectTemplate.as_view(), name="update-effect"),

    ]