from django.contrib import admin

from fromleaf_contactme.models import ContactMePage

class ContactMePageAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'created_at']

admin.site.register(ContactMePage, ContactMePageAdmin)