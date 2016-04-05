from django.contrib import admin

from fromleaf_common.models.user import MemberInfo, ExtraUserInfo, User
from fromleaf_common.models.page import PageData
    

class MemeberInline(admin.StackedInline):
    model = MemberInfo
    verbose_name_plural = 'Create or select Member Information'
    extra = 1
    max_num = extra
    
    
class ExtraUserInfoInline(admin.StackedInline):
    model = ExtraUserInfo
    verbose_name_plural = 'Create or select Extra User Information'
    extra = 1
    max_num = extra
    blank=True
    
    
class UserAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = [MemeberInline, ExtraUserInfoInline]
    

admin.site.register(PageData)  
admin.site.register(User, UserAdmin)

# TODO: After finished development, below code have to be delete.
# admin.site.register(ExtraUserInfo)
# admin.site.register(MemberInfo)
