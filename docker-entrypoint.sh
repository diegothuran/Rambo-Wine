#!/bin/bash

python /manage.py migrate                  # Apply database migrations
python /manage.py collectstatic --noinput  # Collect static files
NEW_RELIC_CONFIG_FILE=newrelic.ini newrelic-admin run-program python /manage.py runserver 0.0.0.0:8000   # Run server
