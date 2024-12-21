from tinymce.widgets import TinyMCE
from django import forms
from django.contrib import admin
from apps.blog.models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        widgets = {"content": TinyMCE()}
        exclude = []

class ArticleAdmin(admin.ModelAdmin):
    form = ArticleForm


admin.site.register(Article, ArticleAdmin)