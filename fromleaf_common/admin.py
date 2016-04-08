from django.contrib import admin

from fromleaf_common.models.user import MemberInfo, ExtraUserInfo, UserSNSInfo, UserInfo
from fromleaf_common.models.page import PageContainer
    
    
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

class UserSNSInfoInline(admin.StackedInline):
    model = UserSNSInfo
    verbose_name_plural = 'Create or select User SNS Information'
    extra = 1
    max_num = extra
    blank=True
    
class ExtraUserAdmin(admin.ModelAdmin):
    inlines = [UserSNSInfoInline]    
    
class UserAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = [MemeberInline]
    

admin.site.register(PageContainer)
admin.site.register(UserInfo, UserAdmin)
admin.site.register(ExtraUserInfo, ExtraUserAdmin)

# TODO: After finished development, below code have to be delete.
# admin.site.register(ExtraUserInfo)
# admin.site.register(MemberInfo)
