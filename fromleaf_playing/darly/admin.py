from django.conf import settings
from django.contrib import admin

from fromleaf_playing.darly.models import DarlyPhoto   
        
class DarlyAdmin(admin.ModelAdmin):
    using = 'darly.db.sqlite3'
    list_display = ['photo_name', 'created_at']    # 레코드 리스트 항목 지정
    list_filter = ['created_at']                      # 필터 사이드 바 추가

admin.site.register(DarlyPhoto, DarlyAdmin)