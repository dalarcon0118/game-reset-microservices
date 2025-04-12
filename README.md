# Game Reset Microservices

## Overview
Game Reset is a multi-tenant microservices application built with Django for managing lottery and gaming operations. The system provides a comprehensive platform for banks, branches, and listeros to manage games, draws, bets, and financial records.

## Features
- **Multi-tenancy**: Isolated environments for different organizations using django-tenant-schemas
- **Hierarchical Structure**: Tree-based organization structure using django-mptt
- **Game Management**: Create and manage different game types
- **Draw Management**: Schedule and manage draws
- **Bet Recording**: Track bets placed by customers
- **Financial Tracking**: Monitor financial statements across the organization
- **Payout Rules**: Configure custom payout rules for different games
- **Number Limits**: Set limits on specific numbers to manage risk

## Architecture
The application follows a microservices architecture with the following components:

- **Authentication**: User management and authentication
- **Structure**: Hierarchical organization management (Banks, Branches, Listeros)
- **Game Type**: Game configuration and management
- **Draw**: Draw scheduling and results
- **Bet**: Bet recording and tracking
- **Payout Rule**: Configuration for game payouts
- **Number Limit Rule**: Risk management for specific numbers
- **Financial Statement**: Financial tracking and reporting

## Technology Stack
- **Backend**: Django, Django REST Framework
- **Database**: PostgreSQL
- **Authentication**: JWT (JSON Web Tokens)
- **Caching**: Redis
- **Message Queue**: RabbitMQ
- **Multi-tenancy**: django-tenant-schemas
- **Tree Structure**: django-mptt

## Getting Started

### Prerequisites
- Python 3.8+
- PostgreSQL
- Redis
- RabbitMQ

### Installation
1. Clone the repository
2. Create a virtual environment: python -m venv venv
source venv/bin/activate
3. Install dependencies:pip install -r requirements.txt

4. Configure environment variables (see .env.example)
5. Run migrations:python manage.py migrate_schemas --shared
6. Create a superuser: python manage.py createsuperuser

7. Run the development server: python manage.py runserver

## API Documentation
API documentation is available at `/api/docs/` when the server is running.

## License
[Specify your license here]