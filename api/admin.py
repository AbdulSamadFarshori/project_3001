from django.contrib import admin
from .models import main_data,  response, keywords, CompletedCase, ReplyData, ReplyThread
 
@admin.register(main_data)
class MainDataAdmin(admin.ModelAdmin):
  list_display = ['id', 'heading', 'sub_heading', 'main_problem' ,'author_name']

@admin.register(ReplyData)
class MainDataAdmin(admin.ModelAdmin):
  list_display = ['id', 'case_id', 'author', 'recipient' ,'reply']

@admin.register(ReplyThread)
class MainDataAdmin(admin.ModelAdmin):
  list_display = ['id', 'case_id', 'author', 'recipient' ,'reply']

@admin.register(response)
class ResponseAdmin(admin.ModelAdmin):
  list_display = ['case_id', 'counsellor', 'petient_asking', 'relavent_score' ,'summary', 'reply']


@admin.register(keywords)
class KeywordAdmin(admin.ModelAdmin):
  list_display = ['case_id', 'keyword']


@admin.register(CompletedCase)
class CompleteCasesAdmin(admin.ModelAdmin):
  list_display = ['case_id']
