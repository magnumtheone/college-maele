from django.db import models
from django.utils import timezone

class Article(models.Model):
    titre = models.CharField(max_length=255)
    contenu = models.TextField()
    date_publication = models.DateTimeField(default=timezone.now)
    auteur = models.CharField(max_length=150, default='Admin')  # plus tard possible FK vers User
    image = models.ImageField(upload_to='articles/images/', blank=True, null=True)

    def __str__(self):
        return self.titre

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"

class Video(models.Model):
    article = models.ForeignKey(Article, related_name='videos', on_delete=models.CASCADE)
    titre = models.CharField(max_length=255, blank=True)
    fichier = models.FileField(upload_to='articles/videos/', blank=True, null=True)
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.titre or (self.url or f"Vidéo {self.pk}")