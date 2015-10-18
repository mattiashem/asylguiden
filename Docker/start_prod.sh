#!/bin/bash
#
#
# Startup script for the prod server
cd /var/www/asylguiden
gunicorn --log-file=- onbytes.wsgi:application