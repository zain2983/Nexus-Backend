from pathlib import Path
import os
from dotenv import load_dotenv
from rich import print

load_dotenv()  # Loads variables from .env file in development

BASE_DIR = Path(__file__).resolve().parent.parent

# Use env secret key in production, fallback to insecure one in local dev
SECRET_KEY = os.getenv("SECRET_KEY", "django-insecure-k+g7%o4xu-9n*=5guqgb$8%nwfqyb*41%n1nu(i!3es2c#sx%9")

# DEBUG = os.getenv("DEBUG", "True") == "True"
# ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "127.0.0.1,localhost").split(",")
# CORS_ALLOWED_ORIGINS = os.getenv("CORS_ALLOWED_ORIGINS", "http://localhost:5173").split(",")

# ALLOWED_HOSTS = ['*']
# CORS_ALLOW_ALL_ORIGINS = True



DEBUG = False

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    "0.0.0.0",
    "nexus-backend-bye3.onrender.com",
    

]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "https://nexus-frontend-eta.vercel.app/",
    "https://nexus-frontend-eta.vercel.app/auth/login",
    "https://nexus-frontend-eta.vercel.app/auth/signup",
]

CSRF_TRUSTED_ORIGINS = [
    "https://nexus-frontend-eta.vercel.app",
]



sepr = "=" * 50
print(sepr)
print(f"SECRET_KEY: {SECRET_KEY}")  # Debugging line to check secret key
print(f"DEBUG: {DEBUG}")  # Debugging line to check debug status
print(f"CORS_ALLOWED_ORIGINS : {CORS_ALLOWED_ORIGINS}")
print(f"ALLOWED_HOSTS: {ALLOWED_HOSTS}")  # Debugging line to check allowed hosts
print(sepr)

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'users',

    'corsheaders',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # Must be high
    'django.middleware.common.CommonMiddleware',

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'backend.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
    ],
}

# Disable CSRF for API endpoints
CSRF_TRUSTED_ORIGINS = os.getenv("CORS_ALLOWED_ORIGINS", "http://localhost:5173").split(",")

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
