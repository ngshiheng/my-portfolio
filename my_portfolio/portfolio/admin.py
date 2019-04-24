from django.contrib import admin
from .models import Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'URL')


admin.site.register(Project, ProjectAdmin)
