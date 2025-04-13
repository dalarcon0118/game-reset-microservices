#!/bin/bash

# Check if Docker is running
if ! docker info > /dev/null 2>&1; then
  echo "Docker is not running. Please start Docker and try again."
  exit 1
fi

# Start containers in detached mode
echo "Starting containers..."
docker-compose up -d --build

# Wait a moment for services to be ready
echo "Waiting for services to start..."
sleep 15

# First, create the database schema
echo "Creating database schema..."
docker-compose exec -T db psql -U postgres -d gamereset -c "CREATE SCHEMA IF NOT EXISTS public;"

# Create migrations for all apps if they don't exist
echo "Making migrations for all apps..."
docker-compose exec -T web python manage.py makemigrations

# Run standard Django migrations
echo "Running standard migrations..."
docker-compose exec -T web python manage.py migrate

# Now migrate shared apps
echo "Setting up shared apps..."
docker-compose exec -T web python manage.py migrate_schemas --shared

# Create a tenant
echo "Creating a default tenant..."
docker-compose exec -T web python manage.py shell -c "
from tenants.models import Client
try:
    if not Client.objects.filter(schema_name='public').exists():
        tenant = Client(domain_url='localhost', schema_name='public', name='Public Tenant')
        tenant.save()
        print('Default tenant created')
    else:
        print('Default tenant already exists')
except Exception as e:
    print(f'Error creating tenant: {e}')
"

# Run migrations for tenant apps
echo "Migrating tenant apps..."
docker-compose exec -T web python manage.py migrate_schemas --tenant

# Create a superuser
echo "Creating superuser..."
docker-compose exec web python manage.py shell -c "
from django.contrib.auth.models import User
from tenant_schemas.utils import schema_context
try:
    with schema_context('public'):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'admin')
            print('Superuser created successfully')
        else:
            print('Superuser already exists')
except Exception as e:
    print(f'Error creating superuser: {e}')
"