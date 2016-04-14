from django.contrib import admin

from fromleaf_myskill.models import MySkillPage, SkillSet


class MySkillSetInline(admin.TabularInline):
    model = SkillSet
    verbose_name_plural = 'Create My Skill' 
    extra = 1
        
            
class MySkillPageAdmin(admin.ModelAdmin):
    list_display = ['id', 'page_name', 'page_describe', 'created_at']
    inlines = [MySkillSetInline]
    
admin.site.register(MySkillPage, MySkillPageAdmin)
