from django.contrib import admin
from .models import Subscriber


class SubscriberAdmin(admin.ModelAdmin):

    readonly_fields = ('email', )

    # Не создавать подписчиков из админки
    def has_add_permission(self, request):
        return False

admin.site.register(Subscriber, SubscriberAdmin)
