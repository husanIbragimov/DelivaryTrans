from django.contrib import admin
from apps.about_company.models import AboutCompany, AboutCompanyImages


class AboutCompanyImagesInline(admin.TabularInline):
    model = AboutCompanyImages
    extra = 1


class AboutCompanyAdmin(admin.ModelAdmin):
    inlines = [AboutCompanyImagesInline]
    list_display = ('id', 'title', 'date_created', 'is_active')
    readonly_fields = ('date_created',)


admin.site.register(AboutCompany, AboutCompanyAdmin)
