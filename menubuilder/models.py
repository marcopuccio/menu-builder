# -*- encoding:utf-8 -*-

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.db import models
from django.template.defaultfilters import slugify
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Menu(models.Model):
    """
    Wrapper of menues. The instances of this model will have a lot of items
    related to it for make menues. 
    """
    menu_text = models.CharField(max_length = 255)
    slug = models.SlugField(max_length = 255)

    wrap_tag = models.CharField("HTML Tag", max_length = 255, default="ul")
    class_tag = models.CharField("HTML Class", max_length = 255, default="", blank=True, null=True)
    attrs_tag = models.CharField("HTML Attrs", max_length = 255, default="", blank=True, null=True)

    def __str__(self):
        return self.menu_text

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.menu_text)
        super(Menu, self).save(*args,**kwargs)


@python_2_unicode_compatible
class Item(models.Model):
    """
    Item instances will be related to a Menu model instance to build dynamic
    navigation.
    """
    LINK_TARGET_CHOICES = (
            (None, u"Nothing"),
            ("_blank", u"New tab"),
            ("_new", u"New window"),
    )

    menu = models.ForeignKey(Menu)
    item_text = models.CharField("Title", max_length = 255)
    slug = models.SlugField(max_length = 255)
    url = models.URLField("URL alternativa", blank=True, null=True)

    # Item html handle.
    wrap_tag = models.CharField("HTML Tag", max_length = 10, default="li")
    class_tag = models.CharField("HTML Class", max_length = 100, default="", blank=True, null=True)
    attrs_tag = models.CharField("HTML Attrs", max_length = 100, blank=True, null=True)
    is_link = models.BooleanField("Es link", default=True)
    link_target = models.CharField("Open Mode", max_length=40, blank=True,  null=True, choices=LINK_TARGET_CHOICES)

    # Generic relation
    content_type = models.ForeignKey(ContentType, blank=True, null=True)
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_object = GenericForeignKey('content_type', 'object_id')

    sort_order = models.IntegerField('Sort Order', blank=True, null=True, default=1)
    class Meta:
        ordering = ['sort_order', 'slug']

    def __str__(self):
        return "%s - %s" % (self.menu, self.item_text)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.item_text)
        super(Item, self).save(*args,**kwargs)

    def get_absolute_url(self):
        if self.url:
            return self.url 
        try:
            url = self.content_object.get_absolute_url()
        except:
            try:
                url = self.content_object.url
            except:
                url = "/%s/" % self.slug

        return url
    
    def is_menu(self):
        """
        <Boolean> - Menu nesting. 
        """
        return self.content_type and isinstance(self.content_object, Menu)
