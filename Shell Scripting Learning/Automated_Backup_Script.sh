##########
# Automated Backup Script
# This script takes a backup of a directory and stores it in a specified backup location.
##########


#!/bin/bash

# Variables

SOURCE_DIR="/var/www/html"
BACKUP_DIR="/backup"
DATE=$(date +%F)

tar -czf "$BACKUP_DIR/backup-$DATE.tar.gz" "$SOURCE_DIR"

echo "Backup completed successfully on $DATE"
