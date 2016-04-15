from django.contrib import admin

from fromleaf_history.models import HistoryPage, Company, Project

class ProjectInline(admin.TabularInline):
    model = Project
    verbose_name_plural = 'create Project'


class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'created_at']
    inlines = [ProjectInline]

            
class HistoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'page_name', 'page_describe', 'created_at']
    
admin.site.register(HistoryPage, HistoryAdmin)
admin.site.register(Company, CompanyAdmin)