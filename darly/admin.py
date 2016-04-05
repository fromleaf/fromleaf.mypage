from django.contrib import admin
from darly.models import DarlyPhoto

class DarlyAdmin(admin.ModelAdmin):
    list_display = ['photo_name', 'created_at']    # 레코드 리스트 항목 지정
    list_filter = ['created_at']                      # 필터 사이드 바 추가
    

admin.site.register(DarlyPhoto, DarlyAdmin)