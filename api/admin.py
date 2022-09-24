from django.contrib import admin
from .models import (main_data, 
                    response, NotCompletedStatus, 
                    keywords, UserConfig, 
                    CompletedCase, JWTToken, 
                    ReplyData, Effect, Cause,
                    ReplyThread, History,
                    LinkConfig, PatientAskingForKeyword
                    IntentData, PatientAskingFor
                    EntityData, CauseKeyword)
 
@admin.register(main_data)
class MainDataAdmin(admin.ModelAdmin):
  list_display = ['id', 'title', 'sub_heading', 'main_problem' ,'author_name']

@admin.register(ReplyData)
class ReplyDataAdmin(admin.ModelAdmin):
  list_display = ['case_id', 'author', 'recipient' ,'reply']

@admin.register(ReplyThread)
class ReplyThreadAdmin(admin.ModelAdmin):
  list_display = ['reply_id', 'author', 'recipient' ,'reply']

@admin.register(response)
class ResponseAdmin(admin.ModelAdmin):
  list_display = ['case_id', 'counselor', 'patient_asking', 'patient_need', 'relavent_score' ,'summary', 'reply']

@admin.register(keywords)
class KeywordAdmin(admin.ModelAdmin):
  list_display = ['case_id', 'keyword']

@admin.register(CompletedCase)
class CompleteCasesAdmin(admin.ModelAdmin):
  list_display = ['case_id']

@admin.register(LinkConfig)
class LinkConfigAdmin(admin.ModelAdmin):
  list_display = ['id', 'title', 'heading', 'main_status' ,'reply_status']

@admin.register(IntentData)
class IntentDataAdmin(admin.ModelAdmin):
  list_display = ['id', 'case_id', 'intent']

@admin.register(EntityData)
class EntityDataAdmin(admin.ModelAdmin):
  list_display = ['id', 'case_id', 'entity']

@admin.register(NotCompletedStatus)
class NotCompletedStatusAdmin(admin.ModelAdmin):
  list_display = ['id', 'case_id', 'intent', 'symptoms', 'cause', 'patient_asking_for', 'history', 'effect']

@admin.register(UserConfig)
class UserConfigAdmin(admin.ModelAdmin):
  list_display = ['id', 'username', 'case_id']

@admin.register(JWTToken)
class JWTTokenAdmin(admin.ModelAdmin):
  list_display = ['id', 'refresh_token', 'access_token']

@admin.register(Effect)
class EffectAdmin(admin.ModelAdmin):
  list_display = ['id', 'case_id', 'keyword']

@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
  list_display = ['id', 'case_id', 'keyword']

@admin.register(PatientAskingForKeyword)
class PatientAskingForKeywordAdmin(admin.ModelAdmin):
  list_display = ['id', 'case_id', 'keyword']

@admin.register(PatientAskingFor)
class PatientAskingForAdmin(admin.ModelAdmin):
  list_display = ['id', 'case_id', 'asking']

@admin.register(CauseKeyword)
class CauseKeywordAdmin(admin.ModelAdmin):
  list_display = ['id', 'case_id', 'keyword']

@admin.register(Cause)
class CauseAdmin(admin.ModelAdmin):
  list_display = ['id', 'case_id', 'cause']