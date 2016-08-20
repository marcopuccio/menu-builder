# -*- coding:utf-8 -*-

from django.contrib import admin
from django.db import models

from menubuilder.models import Menu, Item


class ItemInline(admin.StackedInline):
    """
    Admin customization to Stacked Items.
    """
    model = Item
    extra = 2
    fieldsets = [
        (None, {
            'fields': [
                ('item_text', 'slug'),
                'url',
                ('content_type', 'object_id'),
                ('wrap_tag', 'class_tag'),
                ('attrs_tag'),
                ('is_link', 'link_target','sort_order'),
            ]
        })
    ]
    prepopulated_fields = {'slug': ('item_text',)}



@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    """
    Admin customization for Menu objects.
    """
    fieldsets = [
        (None, {
            'fields': [
                'menu_text',
                'slug',
                'wrap_tag',
                'class_tag',
                'attrs_tag',
            ]
        })
    ]
    list_display = ('id', 'menu_text', 'slug')
    prepopulated_fields = {'slug': ('menu_text',)}
    inlines = [
        ItemInline
    ]