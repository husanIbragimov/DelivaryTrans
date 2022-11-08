from django.contrib import admin
from apps.blog.models import Category, Blog, BlogImages


class BlogImagesInline(admin.TabularInline):
    model = BlogImages
    extra = 1


class BlogAdmin(admin.ModelAdmin):
    inlines = [BlogImagesInline]
    list_display = ('id', 'title', 'category', 'date_created', 'is_active')
    readonly_fields = ('date_created',)


admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)
