from django.contrib import admin
from apps.autopark.models import Car, CarImages, Category


class CarImagesImagesInline(admin.TabularInline):
    model = CarImages
    extra = 1


class CarAdmin(admin.ModelAdmin):
    inlines = [CarImagesImagesInline]
    list_display = ('id', 'title', 'category', 'car_weight', 'car_length', 'date_created', 'is_active')
    readonly_fields = ('date_created',)


admin.site.register(Car, CarAdmin)
admin.site.register(Category)

