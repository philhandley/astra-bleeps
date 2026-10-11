#!/usr/bin/env bash
# Offline test: headless Edge registers sw.js and reports what it cached. Needs: python tools/slowserve.py 8201
OUT="/c/Users/Phil/AppData/Local/Temp/claude/C--1-Astra-Nova---Finn/e20cb3e3-1b2d-450d-ba32-499d4acf2af3/scratchpad/shots"
PROF="$OUT/profile-edge-sw-$$"; rm -rf "$PROF"
timeout 150 "/c/Program Files (x86)/Microsoft/Edge/Application/msedge.exe" --headless=new --no-first-run --user-data-dir="$PROF" --dump-dom "http://127.0.0.1:8201/dev/test-sw.html?hold=35" 2>/dev/null | grep -o "SWTEST [^<]*" | grep -v "a.join"
rm -rf "$PROF"
