from django.contrib import admin
from .models import Projects, Review, Tag

class ProjectsAdmin(admin.ModelAdmin):
    list_display = ['title', 'demo_link','source_link','total_vote', 'vote_ratio', 'created']
    list_display_links = ['title', 'source_link']
    ordering = ['-created']

admin.site.register(Projects, ProjectsAdmin)
admin.site.register(Review)
admin.site.register(Tag)