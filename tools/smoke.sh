#!/usr/bin/env bash
# Usage: tools/smoke.sh [only=m1,m2] [ms-per-step]
# Runs dev/smoke.html in headless Chrome and prints the SMOKE lines.
OUT="/c/Users/Phil/AppData/Local/Temp/claude/C--1-Astra-Nova---Finn/e20cb3e3-1b2d-450d-ba32-499d4acf2af3/scratchpad/shots"
mkdir -p "$OUT"; PROF="$OUT/profile-smoke-$$"; rm -rf "$PROF"
Q="ms=${2:-700}"; [ -n "$1" ] && Q="$Q&only=$1"
timeout 400 "/c/Program Files/Google/Chrome/Application/chrome.exe" --headless=new --enable-unsafe-swiftshader --use-angle=swiftshader \
  --no-first-run --user-data-dir="$PROF" --window-size=1720,820 --virtual-time-budget=500000 --autoplay-policy=no-user-gesture-required \
  --enable-logging=stderr --v=0 --screenshot="$OUT/smoke.png" "http://127.0.0.1:8200/dev/smoke.html?$Q" 2>&1 | grep -E "SMOKE" | sed -E 's/^.*SMOKE /SMOKE /; s/", source.*$//'
rm -rf "$PROF"
