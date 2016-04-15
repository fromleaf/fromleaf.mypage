from django.contrib import admin

from fromleaf_common.models.user import MemberInfo, ExtraUserInfo, UserSNSInfo, Education
from fromleaf_common.models.page import PageContainer
    

class UserSNSInfoInline(admin.TabularInline):
    model = UserSNSInfo
    verbose_name_plural = 'Create or select User SNS Information'
    extra = 1
    
class EducationInline(admin.TabularInline):
    model = Education
    verbose_name_plural = 'Create or select Education'
    extra = 1
    
class ExtraUserAdmin(admin.ModelAdmin):
    inlines = [UserSNSInfoInline, EducationInline]     

class MemberAdmin(admin.ModelAdmin):
    list_display = ['email', 'grade']

class UserSNSInfoAdmin(admin.ModelAdmin):
    list_display = ['sns_name', 'sns_address', 'user_id']

admin.site.register(PageContainer)
admin.site.register(MemberInfo, MemberAdmin)
admin.site.register(UserSNSInfo, UserSNSInfoAdmin)
admin.site.register(ExtraUserInfo, ExtraUserAdmin)

# TODO: After finished development, below code have to be delete.
# admin.site.register(ExtraUserInfo)
# admin.site.register(MemberInfo)
