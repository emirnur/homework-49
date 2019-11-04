from django.contrib import admin
from webapp.models import TrackerIssue, Type, Status, Project, Team


class TrackerIssueAdmin(admin.ModelAdmin):
    list_display = ['pk', 'summary', 'description', 'status', 'type', 'created_at']
    list_filter = ['summary', 'status']
    list_display_links = ['pk', 'summary']
    search_fields = ['summary', 'description']
    exclude = []
    readonly_fields = ['created_at']


admin.site.register(TrackerIssue, TrackerIssueAdmin)
admin.site.register(Type)
admin.site.register(Status)
admin.site.register(Project)
admin.site.register(Team)