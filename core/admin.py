from django.contrib import admin
from core.models import *
from django.contrib import messages
from django.utils.translation import ngettext

@admin.register(Resident)
class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [("Main", {"fields": ['user', 'num']})]

@admin.register(Project)
class ManagerAdmin(admin.ModelAdmin):
    fieldsets = [("Main", {"fields": ['name', 'desc', 'cost', 'done']})]

@admin.register(Transactions)
class ManagerAdmin(admin.ModelAdmin):
    fieldsets = [("Main", {"fields": ['name','resident','project','cost']})]
