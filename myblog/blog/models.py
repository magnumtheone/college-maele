from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from ckeditor.fields import RichTextField

class Article(models.Model):
    titre = models.CharField(max_length=200)
    contenu = RichTextField()  # 👈 permet le texte riche (gras, italique, etc.)
    auteur = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', blank=True, null=True)  # 👈 pour une image principale
    video = models.FileField(upload_to='videos/', blank=True, null=True)   # 👈 pour une vidéo
    date_publication = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.titre

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titre)
        super().save(*args, **kwargs)
