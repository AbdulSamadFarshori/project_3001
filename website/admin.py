from django.contrib import admin
from .models import Cookies, FingerPrints
 
@admin.register(Cookies)
class CookiesAdmin(admin.ModelAdmin):
  list_display = ['id', 'set_cookies']

  class Meta:
        verbose_name_plural = "Cookies"


@admin.register(FingerPrints)
class FingerPrintsAdmin(admin.ModelAdmin):
  list_display = ['date_time','user', 'ip']

  class Meta:
        verbose_name_plural = "Finger Prints"

