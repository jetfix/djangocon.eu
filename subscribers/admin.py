from django.contrib import admin

from subscribers.models import Subscriber

class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'timestamp')
    readonly_fields = ('hash',)

admin.site.register(Subscriber, SubscriberAdmin)
