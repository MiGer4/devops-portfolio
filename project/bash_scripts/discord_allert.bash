#!/bin/bash
THRESHOLD=10
WEBHOOK_URL="https://discordapp.com/api/webhooks/1417569319583223848/0w0WnwhxHzqXXR9nKgr4tmxh9-I8l4h--yRbHCzDedeHQT8Qr6hafujQ5syCxtA3LDXd"
USAGE=$(df --output=pcent,target / | tail -n1 | awk '{print $1}' | tr -d '%')
if (( USAGE > THRESHOLD )); then
MESSAGE="⚠ Disk Alert! Root partition '/' usage is at ${USAGE}% (threshold: ${THRESHOLD}%)"
curl -H "Content-Type: application/json" \
-X POST \
-d "{\"content\": \"$MESSAGE\"}" \
"$WEBHOOK_URL"
fi