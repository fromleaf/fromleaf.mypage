from django.contrib import admin

from fromleaf_career.models import CareerPage, Company, Project

class ProjectInline(admin.StackedInline):
    model = Project
    verbose_name_plural = 'create Project'
    extra = 1
    
class CompaynInline(admin.StackedInline):
    model = Company
    verbose_name_plural = 'create Company'
    extra = 1

class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'created_at']
    inlines = [ProjectInline]

            
class CareerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'created_at']
    inlines = [CompaynInline]
    
admin.site.register(CareerPage, CareerAdmin)
admin.site.register(Company, CompanyAdmin)