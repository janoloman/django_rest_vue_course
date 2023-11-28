#!/bin/bash

# Save current directory
# current_dir=$(pwd)

# Run django server
source ~/django_rest_vue_course/03-DRF-1/venv/bin/activate
python3 newsapi/manage.py runserver

# Restore the original directory
# cd "$current_dir"