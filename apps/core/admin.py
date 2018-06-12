from django.contrib import admin
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory

from .models import Article, Category


class CategoryAdmin(TreeAdmin):
    form = movenodeform_factory(Category)


class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal = ('categories',)


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
