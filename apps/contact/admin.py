from django.contrib import admin
from apps.contact.models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'phone_number', 'from_here', 'to_here', 'status', 'date_created')
    readonly_fields = ('date_created',)


admin.site.register(Contact, ContactAdmin)
