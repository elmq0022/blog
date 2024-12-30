from django import forms
from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from tinymce.widgets import TinyMCE

from apps.blog.models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        widgets = {"content": TinyMCE()}
        exclude = []


class ArticleAdmin(admin.ModelAdmin):
    form = ArticleForm


admin.site.register(Article, ArticleAdmin)


class FlatPageForm(forms.ModelForm):
    class Meta:
        model = FlatPage
        widgets = {'content': TinyMCE(attrs={'cols': 160, 'rows': 30})}
        exclude = []


class CustomFlatPateAdmin(FlatPageAdmin):
    form = FlatPageForm


admin.site.unregister(FlatPage)
admin.site.register(FlatPage, CustomFlatPateAdmin)
