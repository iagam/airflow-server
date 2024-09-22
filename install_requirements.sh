#!/bin/bash

# Navigate to the current directory where the script is located (i.e., your repository folder)
cd "$AIRFLOW_DAGS_PATH"

# Pull the latest changes from GitHub
git pull origin main

# Install or upgrade only the new/modified dependencies from requirements.txt
pip install --upgrade -r requirements.txt

# Restart Airflow Scheduler to reflect any new changes in DAGs
pkill -f "airflow scheduler"
airflow scheduler &
