from django.contrib import admin
from .models import Article, Video

class VideoInline(admin.TabularInline):
    model = Video
    extra = 1

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    """
    Configuration de l'affichage de l'administration pour le modèle Article.
    Permet de personnaliser la liste des articles affichés.
    """
    # Définit les champs à afficher dans la liste des articles
    list_display = ('titre', 'auteur', 'date_publication')
    
    # Ajoute un filtre sur la date de publication
    list_filter = ('date_publication',)
    
    # Ajoute une barre de recherche pour le titre et le contenu
    search_fields = ('titre', 'contenu', 'auteur')
    
    # Définit les champs qui seront des liens vers la page de modification
    list_display_links = ('titre',)
    
    # Ajoute une hiérarchie de dates pour la navigation
    date_hierarchy = 'date_publication'
    inlines = [VideoInline]
    fieldsets = (
        (None, {'fields': ('titre', 'contenu', 'auteur', 'image')}),
        ('Dates', {'fields': ('date_publication',)}),
    )

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('titre', 'article', 'fichier', 'url')
