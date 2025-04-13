from pathlib import Path
from datetime import timedelta
from decouple import config, Csv

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config('SECRET_KEY')

DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())

INSTALLED_APPS = [
    'tenant_schemas',  # Move to the top before Django core apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_simplejwt',
    'tenants',
    'core',
    'authentication',
    'game_type',
    'winning_record',
    'bet',
    'structure',
    'origin',
    'draw',
    'payout_rule',
    'number_limit_rule',
    'mptt',
    'financial_statement',  # Add this line
]

# Also add to TENANT_APPS if it should be tenant-specific
TENANT_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'authentication',
    'structure',
    'origin',
    'draw',
    'game_type',
    'winning_record',
    'bet',
    'payout_rule',
    'financial_statement',  # Add this line
]

MIDDLEWARE = [
    'tenant_schemas.middleware.TenantMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Add TEMPLATES configuration
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

TENANT_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'authentication',
    'structure',
    'origin',
    'draw',
    'game_type',
    'winning_record',
    'bet',
    'payout_rule',
]

TENANT_MODEL = "tenants.Client"
PUBLIC_SCHEMA_NAME = config('PUBLIC_SCHEMA_NAME', default='public')
DEFAULT_FILE_STORAGE = 'tenant_schemas.storage.TenantFileSystemStorage'

SHARED_APPS = [
    'tenant_schemas',
    'tenants',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
]

DATABASE_ROUTERS = ['tenant_schemas.routers.TenantSyncRouter']

# Add database configuration
DATABASES = {
    'default': {
        'ENGINE': 'tenant_schemas.postgresql_backend',
        'NAME': config('DB_NAME', default='gamereset'),
        'USER': config('DB_USER', default='postgres'),
        'PASSWORD': config('DB_PASSWORD', default='postgres'),
        'HOST': config('DB_HOST', default='db'),
        'PORT': config('DB_PORT', default='5432', cast=int),
    }
}

# Redis Configuration
REDIS_HOST = config('REDIS_HOST', default='redis')
REDIS_PORT = config('REDIS_PORT', default='6379', cast=int)

# RabbitMQ Configuration
RABBITMQ_CONNECTION = {
    'host': config('RABBITMQ_HOST', default='rabbitmq'),
    'port': config('RABBITMQ_PORT', default='5672', cast=int),
    'username': config('RABBITMQ_USER', default='guest'),
    'password': config('RABBITMQ_PASSWORD', default='guest')
}

# Cache Configuration
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': f'redis://{REDIS_HOST}:{REDIS_PORT}/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Root URL Configuration
ROOT_URLCONF = 'config.urls'