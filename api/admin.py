from django.contrib import admin
from .models import main_data, response, keywords, CompletedCase
 
@admin.register(main_data)
class MainDataAdmin(admin.ModelAdmin):
  list_display = ['id', 'heading', 'sub_heading', 'main_problem' ,'author_name']

  class Meta:
        verbose_name_plural = "Main Data"


@admin.register(response)
class ResponseAdmin(admin.ModelAdmin):
  list_display = ['case_id', 'counsellor', 'petient_asking', 'relavent_score' ,'summary', 'reply']

  class Meta:
        verbose_name_plural = "Responses"

@admin.register(keywords)
class KeywordAdmin(admin.ModelAdmin):
  list_display = ['case_id', 'keyword']

  class Meta:
        verbose_name_plural = "Keywords"


@admin.register(CompletedCase)
class CompleteCasesAdmin(admin.ModelAdmin):
  list_display = ['case_id']
 