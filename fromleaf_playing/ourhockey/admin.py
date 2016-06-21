from django.contrib import admin

from fromleaf_playing.ourhockey.models.Member import Player, Person, Member, Attendance
from fromleaf_playing.ourhockey.models.Post import Post
from fromleaf_playing.ourhockey.models.GameDay import GameDay

class PeronsInline(admin.TabularInline):
    model = Person
    verbose_name_plural = 'Input Person Information' 
    extra = 1
    max_num = extra
    
class PlayerInline(admin.TabularInline): 
    model = Player
    verbose_name_plural = 'Input Player Information' 
    extra = 1
    max_num = extra  
            
class MemberAdmin(admin.ModelAdmin):
    using = 'ourhockey'
    list_display = ['id', 'level', 'duty']
    inlines = [PeronsInline, PlayerInline]
    
class AttendanceAdmin(admin.ModelAdmin):
    using = 'ourhockey'
    list_display = ['get_member_id', 'attended', 'attended_date']
    
    def get_member_id(self, obj):
        return obj.member.id

class GameDayAdmin(admin.ModelAdmin):
    using = 'ourhockey'
    list_display = ['game_day', 'game_type']
    

admin.site.register(Member, MemberAdmin)
admin.site.register(Attendance, AttendanceAdmin)
admin.site.register(GameDay, GameDayAdmin)

admin.site.register(Post)
