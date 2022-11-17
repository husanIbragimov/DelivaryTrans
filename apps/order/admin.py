from django.contrib import admin

from .models import *


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['transaction_id', 'user', 'car', 'title', 'date_created', 'from_here', 'to_here', 'phone_number',
                    'volume_cargo']
    list_filter = ['date_created']
    search_fields = ["title", "user"]


@admin.register(Volume_cargo)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ["title"]


@admin.register(Weight_cargo)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ["title"]


@admin.register(Type_cargo)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ["title"]


@admin.register(Mode_cargo)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ["title"]
