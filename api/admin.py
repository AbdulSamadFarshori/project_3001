from django.contrib import admin
from .models import (main_data, 
                    response, 
                    keywords, 
                    CompletedCase, 
                    ReplyData, 
                    ReplyThread, 
                    LinkConfig, 
                    IntentData,
                    EntityData)
 
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