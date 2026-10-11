#!/usr/bin/env bash
# Runs dev/flow.html (scripted interactions) in headless Chrome and prints the FLOW lines.
OUT="/c/Users/Phil/AppData/Local/Temp/claude/C--1-Astra-Nova---Finn/e20cb3e3-1b2d-450d-ba32-499d4acf2af3/scratchpad/shots"
mkdir -p "$OUT"; PROF="$OUT/profile-flow-$$"; rm -rf "$PROF"
timeout 300 "/c/Program Files/Google/Chrome/Application/chrome.exe" --headless=new --enable-unsafe-swiftshader --use-angle=swiftshader --no-first-run --user-data-dir="$PROF" --window-size=1720,820 --virtual-time-budget=200000 --autoplay-policy=no-user-gesture-required --enable-logging=stderr --v=0 --screenshot="$OUT/flow.png" "http://127.0.0.1:8200/dev/flow.html" 2>&1 | grep -E "FLOW" | sed -E 's/^.*FLOW /FLOW /; s/", source.*$//'
rm -rf "$PROF"
