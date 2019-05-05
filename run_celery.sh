#!/usr/bin/env bash
sleep 5

cd /var/www/continuousPyDj
celery -A continuousPyDj worker -l INFO