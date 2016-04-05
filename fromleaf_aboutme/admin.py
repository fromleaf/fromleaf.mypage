from django.contrib import admin

from fromleaf_common.models.comment import SimpleComment
from fromleaf_common.models.page import PageData
from fromleaf_aboutme.models import AboutMePage 


#class SimpleCommentInline(admin.StackedInline):
class SimpleCommentInline(admin.TabularInline):
#     how can I using these elements in title of SimpleComment.Use by Form??
#     INTRODUCE_MYPAGE = 'INTRODUCE_MYPAGE'
#     SIMPLE_INTRODUCE_MYSELF = 'SIMPLE_INTRODUCE_MYSELF'
#     INTERSTING = 'INTERSTING'
#     CONCLUSION = 'CONCLUSION'
#     
#     TITLE_CHOICES = (
#         (INTRODUCE_MYPAGE, 'Introduce My Page'),
#         (SIMPLE_INTRODUCE_MYSELF, 'Introduce Myself'),
#         (INTERSTING, 'Interesting'),
#         (CONCLUSION, 'Conclusion'),
#     )
    
    model = SimpleComment
    verbose_name_plural = 'create comment' 
    extra = 4
    max_num = extra 
        
            
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ['id', 'page_name', 'page_describe', 'created_at']
    inlines = [SimpleCommentInline]
    
admin.site.register(AboutMePage, AboutMeAdmin)
# TODO: After finished development, below code have to be delete.
# admin.site.register(SimpleComment)