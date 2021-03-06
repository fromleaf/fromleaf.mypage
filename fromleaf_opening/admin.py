from django.contrib import admin

from fromleaf_common.models.comment import SimpleComment
from fromleaf_common.models.page import PageContainer
from fromleaf_opening.models import OpeningPage 


class SimpleCommentInline(admin.TabularInline):
    model = SimpleComment
    verbose_name_plural = 'create comment' 
    extra = 4
    max_num = extra 
        
            
class OpeningAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'created_at']
    inlines = [SimpleCommentInline]
    
admin.site.register(OpeningPage, OpeningAdmin)