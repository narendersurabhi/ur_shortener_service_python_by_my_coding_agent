#!/usr/bin/env sh
set -eu

FRONTEND_URL=${FRONTEND_URL:-http://localhost:3000}
MAX_RETRIES=${MAX_RETRIES:-20}
SLEEP=${SLEEP:-0.5}
TMP=$(mktemp)
trap 'rm -f "$TMP"' EXIT

i=0
while :; do
  i=$((i+1))
  printf 'Checking %s (attempt %d/%s)...\n' "$FRONTEND_URL" "$i" "$MAX_RETRIES" >&2
  status=$(curl -sS -L -w '%{http_code}' -o "$TMP" --max-time 5 "$FRONTEND_URL" || echo "000")
  if [ "$status" = "200" ]; then
    if grep -qiE '<(html|title|form|input)|shorten|shortener' "$TMP"; then
      printf 'Frontend smoke test passed (%s)\n' "$FRONTEND_URL"
      exit 0
    fi
  fi
  if [ "$i" -ge "$MAX_RETRIES" ]; then
    printf 'Frontend did not respond correctly after %s attempts. Last status: %s\n' "$MAX_RETRIES" "$status" >&2
    printf 'Response snippet:\n' >&2
    head -n 200 "$TMP" >&2 || true
    exit 2
  fi
  sleep "$SLEEP"
done
