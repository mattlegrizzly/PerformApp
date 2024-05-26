#!/bin/bash

# Set the PostgreSQL password environment variable
export PGPASSWORD=$PGPASSWORD

# Create a .pgpass file for storing credentials
touch ~/.pgpass
if [ $? -ne 0 ]; then
    echo "Failed to create ~/.pgpass"
    exit 1
fi

# Write the credentials to .pgpass
echo "$PGHOST:*:$PGDATABASE:$PGUSER:$PGPASSWORD" > ~/.pgpass
chmod 0600 ~/.pgpass

# Create a script for creating database backups
touch /backup.sh
if [ $? -ne 0 ]; then
    echo "Failed to create /backup.sh"
    exit 1
fi

# Write the pg_dump command to the script
echo "pg_dump -h $PGHOST -U $PGUSER -d $PGDATABASE -a -w -F p > /backup/db_backup_\$(date +\%Y\%m\%d\%H\%M).sql" > /backup.sh
chmod a+x /backup.sh

# Vérifie si le crontab de l'utilisateur github_runner existe
if sudo -u github_runner crontab -l &> /dev/null; then
    # Si des tâches cron existent, ajoutez la nouvelle tâche
    (sudo -u github_runner crontab -l; echo "0 0 * * * /backup.sh > /var/log/backup.log 2>&1") | sudo -u github_runner crontab -
else
    # Si aucune tâche cron n'existe, créez une nouvelle crontab avec la tâche
    echo "0 0 * * * /backup.sh > /var/log/backup.log 2>&1" | sudo -u github_runner crontab -
fi

# Create the log file if it doesn't exist
if [ ! -f /var/log/backup.log ]; then
    touch /var/log/backup.log
fi

# Continuously output the contents of the log file
cron && tail -f /var/log/backup.log