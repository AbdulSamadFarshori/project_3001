from django.contrib import admin
from .models import Cookies, FingerPrints
 
@admin.register(Cookies)
class CookiesAdmin(admin.ModelAdmin):
  list_display = ['id', 'set_cookies']


@admin.register(FingerPrints)
class FingerPrintsAdmin(admin.ModelAdmin):
  list_display = ['date_time','user', 'ip']

