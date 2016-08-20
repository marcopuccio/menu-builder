# -*- enconding:utf-8 -*-

from django import template

from menubuilder.models import Menu

register = template.Library()

@register.inclusion_tag("tags/menu.html", takes_context=True)
def create_menu(context, slug):
    try:
        menu = Menu.objects.get(slug__iexact=slug)
    except Menu.DoesNotExist:
        menu = '<!-- menu slug %s no existe -->' % slug
    return {
        "request": context.get("request"),
        "default_menu": menu
    }
