#!/bin/bash
BACKUP_DIR=/media/migold/DATA/Misha/programer/university/7semestr/DevOps/lab2/backup
SOURCE_DIR=/media/migold/DATA/Misha/programer/university/7semestr/DevOps/lab2/project

tar -czvf $BACKUP_DIR/project-$(date +%Y%m%d-%H%M%S).tar.gz -C "$SOURCE_DIR" .

LOG_FILE="$BACKUP_DIR/backup.log"
log() {
echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}
if [ ! -d "$SOURCE_DIR" ]; then
log "❌ ERROR: Directory $SOURCE_DIR doesn’t exist!"
exit 1
fi
log "🚀 The start of process…."

find $BACKUP_DIR -type f -name "*.tar.gz" | sort | head -n -5 | xargs -r rm