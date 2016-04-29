from django.contrib import admin

from fromleaf_common.models.comment import SimpleComment
from fromleaf_common.models.page import PageContainer
from fromleaf_aboutme.models import AboutMePage 


class SimpleCommentInline(admin.TabularInline):
    model = SimpleComment
    verbose_name_plural = 'create comment' 
    extra = 4
    max_num = extra 
        
            
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'created_at']
    inlines = [SimpleCommentInline]
    
admin.site.register(AboutMePage, AboutMeAdmin)