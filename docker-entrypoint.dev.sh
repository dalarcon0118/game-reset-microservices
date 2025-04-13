#!/bin/bash

# Start Django development server with auto-reload
watchmedo auto-restart --directory=./ --pattern=*.py --recursive -- python manage.py runserver 0.0.0.0:8000