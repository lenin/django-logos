from django.contrib import admin

from logos.models import Logo

class LogoAdmin(admin.ModelAdmin):
    list_display = ('image', 'is_active', 'upload_date')
    list_filter = ('is_active', 'site')

admin.site.register(Logo, LogoAdmin)
