# Astra Bleeps: build instructions

Read `PLAN.md` first (the specification) and `ENGINE.md` (the contract every module follows). The briefs in `research/` are the source of truth for every fact, number and link; the plan defers to them.

## Who this is for
Finn (6, the Commander), his three-year-old sibling (the Co-pilot) and their dad (the Sound Engineer), together on a Samsung Galaxy Tab in landscape, 10 to 15 minutes at a time. It teaches chiptune (waveforms, pitch, beat and rhythm, melody, chords, game sound effects, a tracker) the Astra Nova way and lets them make songs and the sounds for a little game, Moon Run.

## Sister apps
Astra Finn (`C:\1 Astra Nova - Finn`, the space app and the GitHub Pages repo) and Astra Maths (`C:\1. Astra Nova Synthesis  - Maths Tutor`). This app is published as the `bleeps/` folder of the Astra Finn repo, like Astra Maths in `maths/`. Do not edit the sister apps except to publish into `bleeps/` and to keep the Astra Finn service worker ignoring `/bleeps/`.

## Hard constraints of this machine
- No Node.js and no npm. No build step, bundler or framework.
- Python 3.12 with Pillow for icons (`python tools/make_icons.py`) and `python -m http.server 8200 --bind 127.0.0.1` for local testing (port 8100 is used by the maths app).
- git with Git Credential Manager; no `gh`.

## Technical rules
- Plain HTML, CSS and ES-module JavaScript. No libraries at all; sound is the Web Audio API (`js/core/chip.js`).
- Relative paths everywhere (the app lives under a GitHub Pages sub-path).
- `localStorage` key `astrableeps.v1` only. No backend, accounts, analytics or microphone. Google Fonts (Lexend, Press Start 2P) is the only third-party request.
- Toys follow the contract in `ENGINE.md` section 2 and inject their own scoped CSS.
- Images: public domain or Creative Commons only, credited in `assets/img/CREDITS.md`, 1600 px and 300 KB max.

## Content rules (age first, Astra Nova flavour)
- Mostly playful and hands-on. Every step makes a sound within one tap; every word is read aloud; nothing depends on reading.
- One to three short sentences per card. One number per card with a comparison a six-year-old can picture and a `source` URL from `research/01`.
- Guesses: Commander, then Co-pilot, then Engineer. A miss gets "Ooh, good guess! Listen..." and never a cross.
- Big Questions only in Missions 4 to 7: picture options, no right answer, a reveal that says what real game makers did without crowning an option, written so a crew could split. The Commander's final choice changes Moon Run (`store.state.choices`).
- Every mission ends with a debrief ("What was your favourite part?" plus one question) and a patch.
- Steps for the three-year-old carry `"who": "copilot"`. No scores between the children, no timers they can see, no losing.
- No copyrighted game music. Demo tunes are public domain (Twinkle Twinkle, Mary Had a Little Lamb, Ode to Joy) or original.

## Testing
- `dev/smoke.html` walks every mission step and every studio screen and reports errors (run it headless: see `tools/smoke.sh`).
- `dev/harness.html?toy=<name>&props=<json>` mounts one toy. `dev/audio-test.html` plays every voice, drum, effect and demo song.
- `bash tools/shot.sh <name> "<path>" 1280,800 4000` takes a headless Chrome screenshot (port 8200). Add `?devcrew` to skip crew setup.
- Run `python tools/build_sw.py` after any change, before publishing. Offline test: start `python tools/slowserve.py 8201`, then `bash tools/swtest.sh` (headless Edge, real time). The browser pane cannot register service workers, and headless virtual time stops before caching finishes.
- Headless Chrome freezes the Web Audio clock, so check playback in the browser pane; python's server lets the browser cache ES modules, so force-reload changed modules there.

## Done means
Installed from the public link on the tablet, Mission 1 and the Song Maker work end to end with sound and no console errors, Moon Run plays the crew's sounds, and the app opens with Wi-Fi off after one online visit.
