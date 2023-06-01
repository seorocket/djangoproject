from django.contrib import admin
from .models import *
from rangefilter.filter import DateRangeFilter

seo_fields = [
    'alias',
    'seo_h1',
    'seo_title',
    'seo_description',
    'seo_keywords',
    'content'
]


@admin.register(TextPage)
class TextPageAdmin(admin.ModelAdmin):
    fieldsets = [('Основные', {"fields": ["name"]}), ('SEO информация', {'fields': seo_fields})]

    def get_prepopulated_fields(self, request, obj=None):
        return {"alias": ("name",)}


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    fieldsets = [('Основные', {"fields": ["name", "photo", "dt_create"]}), ('SEO информация', {'fields': seo_fields})]
    readonly_fields = ["dt_create"]

    def get_prepopulated_fields(self, request, obj=None):
        return {"alias": ("name",)}


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    ...


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    ...



@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ['dt_create']

    def get_list_filter(self, request):
        return ('dt_create', DateRangeFilter),
