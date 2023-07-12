from django.contrib import admin
from .models import Profile, Skills

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'email', 'social_github', 'social_website','social_twitter', 'social_linkedIn', 'created',)
    list_display_links = ('user', 'email',)
admin.site.register(Profile, ProfileAdmin)

admin.site.register(Skills)
