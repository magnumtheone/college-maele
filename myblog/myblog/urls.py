from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include  # 👈 include est indispensable

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),  # 👈 cette ligne connecte ton app "blog"
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)