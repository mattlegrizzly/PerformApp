#!/bin/bash

set -e

latest_backup=$(ls -t /db/backup/db_backup_*.sql | head -n1)

if [ -n "$latest_backup" ]; then
    echo "Latest backup file is: $latest_backup"
    # Perform additional actions with the latest backup file
else
    echo "No backup files found. Backup will set to init data"
	latest_backup="/db/init_db.sql"
    # Handle the case when no backup files are present
fi

cp "$latest_backup" /backend/latest_backup.sql
echo "Latest backup copied: $latest_backup"

# Stop the container once the copy is finished
echo "Stopping the container..."
kill 1