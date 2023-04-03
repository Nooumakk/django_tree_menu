from django.contrib import admin
from .models import Menu, Items


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(Items)
class ItemsAdmin(admin.ModelAdmin):
    list_display = ("title", "menu")