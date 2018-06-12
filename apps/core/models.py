from django.db import models
from django.utils.translation import ugettext_lazy as _
from treebeard.mp_tree import MP_Node


class Category(MP_Node):
    name = models.CharField(_('Name'), max_length=255)

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.name


class Article(models.Model):
    sku = models.CharField(_('SKU'), max_length=32, unique=True)
    ean = models.CharField(_('EAN'), max_length=13, unique=True)
    name = models.CharField(_('Name'), max_length=255)
    stock = models.IntegerField(_('Stock quantity'))
    price = models.DecimalField(
        _('Price'),
        decimal_places=2,
        max_digits=7,
    )
    categories = models.ManyToManyField(
        Category,
        verbose_name=_('Categories'),
        blank=True,
    )

    class Meta:
        verbose_name = _('Article')
        verbose_name_plural = _('Articles')

    def __str__(self):
        return self.name
