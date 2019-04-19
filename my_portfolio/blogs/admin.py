from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Title', {'fields': ['title']}),
        ('Other Details', {'fields': ['content', 'date_posted', 'author']}),
    ]

    list_display = ('author', 'title', 'date_posted')


admin.site.register(Post, PostAdmin)
