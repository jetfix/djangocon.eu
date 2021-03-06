from django.contrib import admin
from speakers.models import Speaker

class SpeakerAdmin(admin.ModelAdmin):
    list_display = ('name', 'talk_list', 'email', 'website', 'twitter', 'notified')
    search_fields = ('name',)

admin.site.register(Speaker, SpeakerAdmin)
