#!/bin/bash

# Loop through all YAML files in the fixtures directory
for fixture in fixtures/*.yaml; do
    echo "Loading fixture: $fixture"
    ./prj/manage.py loaddata "$fixture"
done