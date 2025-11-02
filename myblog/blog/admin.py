from django.contrib import admin
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre', 'auteur', 'date_publication')
    list_filter = ('auteur', 'date_publication')
    search_fields = ('titre', 'contenu', 'auteur')
    prepopulated_fields = {'slug': ('titre',)}
    ordering = ('-date_publication',)