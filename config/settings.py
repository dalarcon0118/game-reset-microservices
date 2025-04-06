from pathlib import Path
from datetime import timedelta
from decouple import config, Csv

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config('SECRET_KEY')

DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_simplejwt',
    'tenant_schemas',
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
