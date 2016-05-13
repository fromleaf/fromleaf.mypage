from django.contrib import admin

from fromleaf_playing.ourhockey.models.Player import Player, Person, Member

class PeronsInline(admin.TabularInline):
    model = Person
    verbose_name_plural = 'Input Person' 
    extra = 1
    max_num = extra
    
class MemberInline(admin.TabularInline): 
    model = Member
    verbose_name_plural = 'Input Member' 
    extra = 1
    max_num = extra  
            
class PlayerAdmin(admin.ModelAdmin):
    using = 'ourhockey.db.sqlite3'
    list_display = ['id', 'back_number', 'position', 'created_at']
    inlines = [PeronsInline, MemberInline]

admin.site.register(Player, PlayerAdmin)
