from django.contrib import admin
from tracking.models import Visitor, BannedIP, UntrackedUserAgent
from tracking_cron.models import VisitorTotal
        
class VisitorAdmin(admin.ModelAdmin):
    list_display = ('user', 'ip_address', 'page_views', 'session_start', 'url')
    list_filter = ('user',)
    search_fields = ['user__first_name', 'user__email', 'user__username', 'ip_address',]
        
class VisitorTotalAdmin(admin.ModelAdmin):
    list_display = ('total_user', 'total_page_view', 'date',)
    list_filter = ('date',)
    search_fields = ['date',]
    
admin.site.register(Visitor, VisitorAdmin)
admin.site.register(VisitorTotal, VisitorTotalAdmin)