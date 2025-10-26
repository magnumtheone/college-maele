import os
from pathlib import Path
import dj_database_url
from dotenv import load_dotenv

# Charger les variables d'environnement (.env ou Render)
load_dotenv()

# --- Répertoire principal du projet ---
BASE_DIR = Path(__file__).resolve().parent.parent

# --- Clé secrète (⚠️ à remplacer par une clé d'environnement en production) ---
SECRET_KEY = os.getenv(
    'SECRET_KEY',
    'django-insecure-#@one!jnc*ba%%-fih^jug5y$+%5qgcf(lj95)q5bk*3zizkee'
)

# --- Mode debug ---
DEBUG = os.getenv('DEBUG', 'False') == 'True'

# --- Hôtes autorisés ---
ALLOWED_HOSTS = [
    'college-maele.onrender.com',
    '127.0.0.1',
    'localhost'
]

# --- Applications installées ---
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',  # ton application principale
]

# --- Middleware ---
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # ✅ indispensable sur Render
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# --- URL racine ---
ROOT_URLCONF = 'myblog_project.urls'

# --- Templates (corrigé et renforcé) ---
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # ✅ Permet de charger aussi un dossier global "templates" à la racine
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# --- Fichier WSGI ---
WSGI_APPLICATION = 'myblog_project.wsgi.application'

# --- Base de données (PostgreSQL Render) ---
DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv('DATABASE_URL'),
        conn_max_age=600,
        ssl_require=True
    )
}

# --- Validation des mots de passe ---
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# --- Langue et fuseau horaire ---
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# --- Fichiers statiques (CSS, JS, images) ---
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'blog', 'static'),
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# --- Configuration WhiteNoise ---
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# --- Médias (fichiers uploadés) ---
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# --- Clé primaire par défaut ---
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
