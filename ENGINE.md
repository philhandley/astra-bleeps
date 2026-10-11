# Astra Bleeps engine contract

Read `PLAN.md` first for who the app is for (a 6-year-old Commander, a 3-year-old Co-pilot and a grown-up Sound Engineer on a Samsung tablet, landscape, about 1280 x 800 CSS px) and how missions run. This file is the contract every module follows. Plain ES modules, no build step, no libraries, no npm.

## 1. Files and ownership

| Path | Owner | What |
|---|---|---|
| `js/core/*.js` | Opus (main) | engine: chip, seq, song, store, ui, dom, icons, bots, stickers, patch, runner, notes |
| `js/app.js`, `css/app.css`, `index.html` | Opus (main) | shell, router, home, styles |
| `js/toys/songmaker.js pads.js chords.js jukebox.js wake.js closeeyes.js bonk.js beatmaker.js echo.js` | Opus (main) | studio and mission toys |
| `js/toys/moonrun.js` | Agent A | the game |
| `js/toys/wavedraw.js pulse.js lab.js silly.js detective.js` | Agent B | sound shapes and sound design (`lab.js` also exports `LAB_PRESETS`, `soundArt`, `toRecipe`, used by `detective.js`) |
| `js/toys/highlow.js ladder.js starmaker.js march.js beatpad.js moodmove.js` | Agent C | pitch, beat and movement |
| `content/`, `research/` | Opus (main) | missions and facts |

**Write only your own files.** If you need something in a core file, write your own helper inside your toy instead, and mention it in your final report.

## 2. The toy contract

Every toy is one file in `js/toys/<name>.js`:

```js
export function mount(el, props, api) {
  // el: an empty flex column that fills the space (position: relative). Put everything inside it.
  // props: from the mission JSON step's "props", plus { studio: true } when opened from the Studio.
  // api: see below.
  return { destroy() { /* stop timers, sequencers, listeners, sounds */ } };
}
```

`api`:
- `api.mode`: `'mission'` or `'studio'`.
- `api.crew`: `{ commander, copilot, engineer }` names. Default demo names are Finn, Rosie and Dad; never hard-code names, always use these.
- `api.done(msg?)`: call once the step's goal is reached (the Next button starts to glow and confetti pops). Safe to call more than once. Pass `false` to glow without confetti.
- `api.say(text)`: speak a short line if reading aloud is on (UK voice). One short sentence. Do not call it on every tap.
- `api.log(text)`: add a line to the Crew Log (use for things the crew made or chose).
- `api.toast(text)`: a small message at the bottom.
- `api.kit.get(slot)` / `api.kit.set(slot, value)`: the Moon Run sound kit (section 5).
- `api.setWho(role, label)`: optional; shows whose turn it is in the bottom bar (`'commander' | 'copilot' | 'engineer' | 'everyone'`).

Rules:
1. **Sound first.** Every touch makes a sound within about 50 ms. Trigger sounds on `pointerdown`, not `click`.
2. **No failure.** No "wrong", no red crosses, no scores, no timers the children can see, no lives. A miss gets "Ooh, nearly! Listen again." and another go.
3. **Size.** Anything the 3-year-old taps: at least 96 px, ideally 120+. Everything else at least 64 px. Text at least 22 px. No double-tap, no long-press. Dragging is always optional: a tap must also work.
4. **Words are spoken.** The 3-year-old can't read, so pictures and colour carry meaning; text is a label.
5. **Clean up.** `destroy()` must stop every `setInterval`, `requestAnimationFrame`, `Sequencer` and `window` listener, and call `stopAll()` if the toy made long sounds.
6. **CSS.** Put the toy's CSS in the toy with `injectCSS('t-<name>', css)` (from `dom.js`), scoped under a root class `.t-<name>`. Use the CSS variables from `css/app.css` (below). Don't use `vh/vw` for layout; fill `el` with flexbox so the toy fits any size from 1024 x 600 to 1600 x 1000.
7. **Landscape first**, but nothing may break at 800 px wide.

## 3. Core modules you may import (relative to `js/toys/`: `../core/...`)

### chip.js (the sound chip)
- `ensure()`: create or resume the AudioContext (call inside a pointerdown handler before the first sound; `note()` also calls it).
- `now()`: audio clock in seconds.
- `note({ voice, midi | freq, to, slideTime, at, dur, vol, duty, table, wobble, arp, arpRate, echo, bus, env, short, filter })` returns `{ at, end, stop(t) }`. `voice`: `'bleep' | 'hoot' | 'buzz' | 'fizz' | 'crew'`. `midi` 60 = middle C. `to` slides to another midi note. `duty` for bleep: `0.125 | 0.25 | 0.5`. `table`: a custom wave as an array of -1..1 values (any length; 32 is the Game Boy size). `wobble`: vibrato depth (0..2). `arp`: semitone offsets cycled quickly (a "sparkle"). `echo`: 0..1 send to the echo. `bus`: `'lead' | 'chords' | 'bass' | 'drums' | 'sfx'` (default `'sfx'`).
- `drum(kind, at?, { vol })`: `'boom' | 'tap' | 'tss' | 'crash'`.
- `sfx(recipe, at?, { bus, vol })` returns its length in seconds. Recipe: `{ voice, from, to, len, fx: 'none'|'wobble'|'echo'|'sparkle', duty, notes: [midi, ...] }` (if `notes` is given they play one after another and `from/to` are ignored).
- `hello(bot)`: each bot's signature sound. `BONKS[bot]`, `HELLOS[bot]`: recipes.
- `shape(voice, { duty, table })`: one cycle of a voice's wave (array of -1..1) for drawing.
- `setCrewWave(table)`, `crewWave()`: the crew's drawn wave used by voice `'crew'`.
- `pulseTable(duty)`, `TRIANGLE_TABLE`, `SAW_TABLE`, `noiseTable()`.
- `analyser()`: an AnalyserNode on the master output (for a live scope). `context()`: the AudioContext (or null).
- `stopAll()`: silence everything now. `borrow(bus, at, dur)`: duck one bus for a moment. `muteBus(bus, bool)`.
- `mtof(midi)`, `noteName(midi)` ('C', 'D'...), `noteLabel(midi)` ('C4').

### seq.js
`new Sequencer({ steps: () => n, stepDur: step => seconds, schedule: (step, time, dur) => {...}, onStep: step => {...}, onEnd, loop: true })` then `.start(fromStep)`, `.stop()`, `.playing`. `schedule` must schedule sounds at `time` (audio clock). `onStep` fires on screen when the step sounds (for playheads and animation).

### song.js
- `BOTS[bot]` = `{ name, wave, col, dark, soft, words }`. Colours: bleep red `#ff4f45`, hoot blue `#3b82f6`, buzz yellow `#f5b400`, fizz purple `#8b5cf6`, crew teal `#14b8a6`.
- `NOTE_COL` (Boomwhacker colours by note name), `colourOf(midi)`, `NOTE_WORD`.
- `scaleNotes(scale, count, base=60)`: `'magic'` = C D E G A (no wrong notes), `'all'` = C major. Row 0 is the lowest.
- `CHORDS[key]` = `{ name, sym, root, iv, col, ink, icon, mood }` for `home sunny ready rainy dreamy cloudy` (C F G Am Em Dm).
- `SPEEDS` = snail 70, tortoise 90, cat 110, hare 130, rocket 155 (bpm). `speedIndex(id)`.
- Songs: `emptySong(mode)`, `cleanSong(s)`, `copySong(s)`, `stepsOf(song)`, `stepDur(song, step)`, `scheduleStep(song, step, time, dur, { leadBus })`, `demoSongs()` (ids `demo-moonrun`, `demo-robot`, `demo-twinkle`, `demo-mary`, `demo-ode`, `demo-tiny`), `songLength(song)`.
- `KIT_SLOTS`, `KIT_DEFAULTS` (section 5).

### bots.js
`botSVG(bot, { sleep, table, label })` returns an SVG string of a robot (viewBox 120 x 140). Wrap it in `<div class="bot" data-bot="...">` and call `sing(div, ms)` to make it hop and talk while it sounds. `lcdWave(table, { w, h, cycles, smooth })` returns an SVG string of a wave on a green LCD. `wavePath(table, x, y, w, h, cycles)`. `LCD` = Game Boy greens `{ bg: '#9bbc0f', light: '#8bac0f', dark: '#306230', ink: '#0f380f' }`.

### stickers.js
`sticker(name, { size })` returns a 64 x 64 outlined flat picture. Names: star heart note moon rocket robot sun cloud rain greycloud house snail tortoise cat hare mouse bear bird happy sad both drum flag rock planet bolt flower ghost ear eyes sleep hands split turns highlow together quiet nosound spare speedup.

### dom.js
`h(html)` (one element from an HTML string), `esc(s)`, `S(tag, attrs, children)` (SVG element), `svgRoot(w, h)`, `svgPoint(svg, evt)`, `onTap(el, fn)`, `drag(el, { start, move, end }, svgEl)`, `injectCSS(id, css)`, `clamp`, `sleep`, `reducedMotion()`.

### ui.js
`say(text)` (always speaks), `autoSay(text)` (only if reading aloud is on), `hush()`, `speakButton(getText)`, `toast(text)`, `burst(hostEl, originEl)` (pixel confetti), `modal(title, bodyEl)`.

### icons.js
`icon(name)` returns a 24 x 24 line icon SVG string: home speaker speakerOff back next play stop check star close edit music plus minus trash save refresh help book log list grid wobble echo sparkle slide up down game eyeClosed hand pages drum piano wave volume copy download shuffle long dot eraser.

### store.js
`store.state` (read only for toys except through `api.kit`), `crew()`.

## 4. Look

- Warm cream console (`--bg #ece6da`, `--card #fbf8f2`), dark ink `--ink #1b1b24`, bold 3 px outlines (`--edge`), offset shadow `--pop` (`4px 5px 0 #1b1b24`), radius 18 to 26 px. Chunky buttons: `.btn` (cream), `.btn.primary` (magenta `--a #b0246a`, the console's A button), `.btn.go` (green `--go`), `.btn.big`, `.btn.round`, `.btn.small`, `.btn.on` (selected). The big round "Hear it" button is `.playbig`.
- LCD panels: Game Boy green `--lcd #9bbc0f`, `--lcd-2 #8bac0f`, `--lcd-dark #306230`, `--lcd-ink #0f380f`, bezel `--bezel #4b4b5c`. Class `.lcd` gives a bezel and pixel font.
- Fonts: `var(--font)` Lexend for words; `var(--pixel)` "Press Start 2P" only for short labels (PLAY, numbers on an LCD), never for sentences.
- Robot colours: `--bleep --hoot --buzz --fizz --crew` (and `-dark`, `-soft`). Crew colours: `--cmd` (Commander yellow), `--cop` (Co-pilot pink), `--eng` (Engineer blue). Notes use `NOTE_COL`.
- Stylish, flat, geometric. Not cartoony clip-art, no emoji, no gradients except subtle ones.

## 5. The Moon Run sound kit (`api.kit`)

| Slot | Value |
|---|---|
| `bump` | a recipe (see `sfx`) |
| `wave` | `{ table: [32 numbers -1..1], name: 'Our Bot' }` |
| `star` | a recipe with `notes: [m1, m2]` |
| `beat` | `[[step 0..7, kind 0 boom / 1 tap / 2 tss], ...]` (8 steps) |
| `win` | a Tiny song object (8 steps) |
| `jump` | a recipe |
| `chords` | `[key, key, key, key]` from `CHORDS` |
| `music` | `{ id }` of a saved song in `store.state.songs` |

Crew choices from Big Questions are in `store.state.choices`: `speed` (`'fast' | 'slow' | 'faster'`), `sharing`, `channel` (`'borrow' | 'none' | 'spare'`), `ending`.

## 6. Testing

- A local server runs on port 8200 (`python -m http.server 8200 --bind 127.0.0.1` from the project folder).
- `dev/harness.html?toy=<name>&props=<url-encoded json>` mounts one toy with a fake `api` that prints to the console and an on-screen log.
- `bash tools/shot.sh <name> "dev/harness.html?toy=<name>" 1280,800 4000` takes a headless Chrome screenshot into the scratchpad and prints console lines (look for errors). Check 1280 x 800 and 1024 x 768.
- Headless Chrome can't hear, so check sound code by reading it carefully; make sure no exceptions are thrown when the AudioContext is suspended.
