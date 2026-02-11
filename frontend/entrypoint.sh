#!/bin/sh
set -e
: "${BACKEND_URL:=http://backend:8000}"
cat > /usr/share/nginx/html/env.js <<EOF
window.BACKEND_URL = "${BACKEND_URL}";
EOF
exec nginx -g 'daemon off;'
