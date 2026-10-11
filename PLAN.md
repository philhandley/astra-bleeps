# Astra Bleeps: a chiptune studio for Finn (6), his little co-pilot (3) and Dad

**Status:** build plan, written 11 Oct 2026.
**Builder:** Opus 5.5 builds the engine, the audio chip, the Song Maker, the runner and the game. Haiku 5.5 subagents research facts, photos, videos and early-years teaching in parallel (section 11).
**Source material:** `research/01-chiptune-facts.md` (every number and date, with URLs), `research/02-teaching-young-children.md` (EYFS, KS1, the Model Music Curriculum, what 3 and 6-year-olds can do, kitchen experiments, touch-target sizes), `research/03-videos.md` (verified video IDs). Where this plan and a research file disagree, the research file wins.
**Sister apps:** Astra Finn (space, `C:\1 Astra Nova - Finn`) and Astra Maths (`C:\1. Astra Nova Synthesis  - Maths Tutor`). Same tablet, same crew, same deployment route: the app is published as the `bleeps/` folder of the Astra Finn GitHub Pages site.

---

## 1. The brief in one paragraph

A tablet web app for two children and their dad, used together for 10 to 15 minutes at a time. It turns a grown-up course ("Chip Tunes: Retro Music Composition": waveforms, melodies with pitch and rhythm, chord progressions, game sound effects, a tracker) into something a three-year-old and a six-year-old can do with their fingers and ears. It teaches the Astra Nova way: every mission starts from a real problem ("our game has no sounds!"), the crew guesses before they find out, a few missions have a Big Question with no right answer that the crew votes on and talks about, and every mission ends with the crew making something, a debrief and a patch. Everything they make goes into one shared project, a little space game called **Moon Run**, so by the last mission the crew plays a game whose jump, star, bump and victory sounds and whose music they made themselves. A free-play Studio (Song Maker, Bleep Pads, Sound Lab, Wave Drawer, Jukebox) is always open. It installs on the Samsung tablet from a GitHub Pages link and works offline.

---

## 2. Teaching method: Astra Nova, for a three-year-old and a six-year-old

### 2a. What Astra Nova does (from the sister app's `research/01-astra-nova-method.md`)

Problem first, curiosity before content. Commit to a guess before the answer. Conundrums: a dilemma with three to five options, no right answer, written so a group splits, ending on a question that starts a discussion. "Constructive disagreement". The north star is "super collaborators". Synthesis-style simulations with a real constraint and a rule change halfway. Mistakes expected. No grades, no scores. Reflection at the end of every session: what worked, what didn't, why.

### 2b. Age first

Astra Nova's own Conundrums are written for 9 to 14-year-olds. At three and six, most learning comes from listening, moving, pressing and copying. So, as in Astra Finn (Dad's feedback, 10 Oct), the app is **mostly playful and hands-on**, with the Astra Nova ideas kept light and concrete:

- **Sound first, words second.** Every step makes a sound within one tap. Every word on screen is read aloud. Nothing depends on reading.
- **No wrong notes.** The tune tools use the five "magic notes" (the pentatonic scale C D E G A) by default, so anything the three-year-old taps sounds good. The six-year-old can switch to all eight notes.
- **Guess, then hear.** "Which robot do you think is the buzzy one?" Commander guesses, Co-pilot points, Engineer guesses last, then the reveal plays the sound. A miss gets "Ooh, good guess! Listen..." and never a cross.
- **Move your body.** Stretch up for high notes, crouch for low, march to the beat, freeze when the music stops. This is how three-year-olds learn pitch and pulse (research/02).
- **Big Questions in only four missions.** Picture options, three or four of them, sometimes with a sound to hear for each. Everybody votes, says why out loud, hears the others, and may change their mind for a star. The reveal never says which option was right; it says what real game composers did, which is usually "all of these".
- **Make something every time.** Each mission ends with the crew making one thing for Moon Run or for the Studio.
- **Try it at home.** Kitchen experiments: rice dancing on cling film, a rubber-band guitar, a water-glass xylophone, a pots-and-pans drum kit.
- **Short.** 8 to 15 minutes per mission. Any step can be skipped with Next. The Co-pilot can wander off and come back.

### 2c. The crew (collaborative, never competitive)

| Role | Who | Does |
|---|---|---|
| **Commander** | Finn, 6 | Makes the final call, guesses first, does the trickier "Commander" steps. |
| **Co-pilot** | the three-year-old | Has the big-button steps (marked with a Co-pilot badge), points to guess, presses PLAY. |
| **Sound Engineer** | Dad | Reads when the voice is off, asks "what does it sound like?" and "why?", runs the movement games, types one line into the Crew Log. |

Names are typed on the crew screen. The app never shows a score between anybody. The crew earns patches together.

The Engineer's three rules (crew screen and Engineer's notes):
1. The children have a go first. The Engineer never gives the answer away.
2. Ask "What does it sound like?" and "Why?" more than you explain.
3. There are no wrong notes. Changed minds get a cheer and a star.

### 2d. The mission rhythm (so the crew knows the ritual by mission two)

| Beat | What happens | Astra Nova idea |
|---|---|---|
| **1. The problem** | Moon Run shows up with something missing ("Our robot jumps but makes no sound!"), or a real story from game history. One picture, one sound, one question. | Problem first. |
| **2. Guess** | A predict-before-you-hear question with picture answers. Commander, then Co-pilot, then Engineer. Then the sound plays. | Commit before the reveal. |
| **3. Play and listen** | Two to five hands-on steps: a toy, a listening game, a movement game, a story card with a sound. | Learn by doing. |
| **4. Big Question** (four missions) | A real game-composer dilemma, picture options, everyone votes, says why, may change their mind. Reveal: what real composers did. | Constructive disagreement. |
| **5. Make it** | The crew makes a sound, a beat, a tune or a song and adds it to Moon Run or the Studio. One rule changes halfway in the last mission. | Synthesis: build under a real constraint. |
| **6. Debrief and patch** | "What was your favourite part?" plus one mission question (for Finn: "What worked? What would you change?"). The patch lands on the wall. | Reflection. |

---

## 3. The idea that ties it together: Moon Run, the silent game

Moon Run is a tiny one-button game in chunky pixel art. A little robot runs across the Moon collecting stars. Tap anywhere to jump. Bumping a rock makes a bump and the robot carries on: there is no losing, no lives and no score between players, just a star count for the crew run and a flag at the end.

At the start it is **silent**. Each mission gives it one thing:

| Slot | Made in | What the crew makes |
|---|---|---|
| **Bump** | M1 Meet the Bleep Bots | Choose which robot says "bonk" when you hit a rock. |
| **Our Bot** (Studio instrument) | M2 Sound Shapes | Draw your own sound wave; it becomes a fifth instrument. |
| **Star** | M3 High and Low | Two quick notes: pick which, high or low. |
| **Beat** | M4 Beat and Rhythm | An eight-box drum beat (and the game speed from the Big Question). |
| **Win tune** | M5 Make a Tune | An eight-box tune that plays at the flag. |
| **Jump** | M6 Game Sounds Lab | A jump sound from the Sound Lab recipe (shape, start, slide, length). |
| **Chords** | M7 Happy and Sad Chords | A four-chord loop. |
| **Music** | M8 Our Game, Our Song | The full song: tune, beat, chords and bass on four channels. |

Until a slot is filled, Moon Run uses silence (and, after M1, a default for anything missing, so it is never broken). The home screen shows the game cartridge with its slots lighting up as they fill. "Play Moon Run" is always available.

---

## 4. App map

**Sound Station** (home): the four Bleep Bots on a little stage (tap one and it sings; the Co-pilot's favourite screen), the Moon Run cartridge with its slots and a Play button, the eight mission cartridges, the Studio tiles, the patch wall with Changed-Mind stars, the Crew Log, Engineer's notes. Nothing is locked.

### The four Bleep Bots (the four sound shapes of an old sound chip)

| Bot | Wave | Sound words | Colour | Body |
|---|---|---|---|---|
| **Bleep** | square / pulse | beepy, hollow, like a game | red | a square block |
| **Hoot** | triangle | soft, round, like a flute or an owl | blue | a triangle |
| **Buzz** | sawtooth | bright, buzzy, like a bee or a trumpet | yellow | saw teeth on top |
| **Fizz** | noise | hissy, like the sea; drums and crashes | purple | a fuzzy cloud |
| **Our Bot** | the crew's drawn wave | whatever they draw | teal | made in M2 |

Real chips: the Commodore 64's SID had exactly these four shapes; the NES had two pulse channels, a triangle and noise; the Game Boy had two pulse, one drawable wave and noise (numbers and sources: research/01). Each bot has a little LCD face that shows its wave and wiggles when it sings.

### Mission 1: The Silent Game (what is chiptune? meet the bots)
1. **Problem:** Moon Run plays for ten seconds with no sound at all. "Something's missing. What?" (Story card with the game running.)
2. **Story:** Old game machines had a tiny sound chip. It could only make a few simple sounds at once. Music made with those chips is called chiptune. (Photos: Game Boy, NES, Commodore 64. One number with a comparison.)
3. **Toy, Co-pilot:** Wake up the bots. Tap each sleeping bot; it wakes and sings its sound. All four awake completes the step.
4. **Guess:** "Which bot sounds like a bee?" (Buzz). "Which is the softest?" (Hoot).
5. **Listening game, everyone:** "Close your eyes!" One crew member taps a hidden bot, the other guesses who sang. Swap. (Cards, no score.)
6. **Make:** "When our robot bumps a rock, who says bonk?" Hear each bot's bonk, the Commander chooses. Saved to the Bump slot.
7. **Try it in the game:** Moon Run with the new bump sound.
8. **Debrief and patch: Bleep Crew.** "What was your favourite part?" "Which bot is your favourite, and why?"

### Mission 2: Sound Shapes (waveforms shape sound)
1. **Problem:** "Hoot and Bleep can sing the very same note, but they sound different. How?"
2. **Try it now:** hand on your throat and hum. Feel the buzz? Sound is wiggles in the air.
3. **Story with sound:** a loudspeaker pushes the air in and out. The robots' screens show the wiggles. Square wiggles sound beepy; pointy triangle wiggles sound soft.
4. **Guess:** two wave pictures, one sound: "Which shape made that sound?"
5. **Toy, Co-pilot:** the Wave Drawer. Scribble a wave with your finger and hear it straight away. (The Game Boy really had a drawable wave with 32 steps: research/01.)
6. **Toy, Commander:** skinny and fat squares (the pulse width): the thinner the square, the thinner the sound.
7. **Make:** draw the crew's own wave, name it, and it becomes **Our Bot**, a fifth instrument in the Studio.
8. **Try it at home:** rice on cling film over a bowl, shout near it (or tap a pan), watch the rice dance.
9. **Debrief and patch: Wave Makers.** "What shape is your favourite sound?"

### Mission 3: High and Low (pitch)
1. **Problem:** "A mouse squeaks and a bear growls. Why do they sound so different?"
2. **Move, everyone:** the Engineer plays high and low notes; stretch up tall for high, crouch down small for low.
3. **Story with sound:** fast wiggles make a high sound; slow wiggles make a low sound (the screen squeezes the wave as the note goes up). One number: concert A wiggles 440 times a second (research/01).
4. **Guess, Co-pilot:** "Mouse or bear?" Two animal pictures, a high or low note.
5. **Toy:** the Pitch Ladder: slide your finger up the ladder, the sound goes up. The Lift game: two notes, did it go up or down?
6. **Make:** the Star sound: two quick notes. Choose the first and second step on the ladder (up sounds happy). Saved to the Star slot. Test in Moon Run.
7. **Try it at home:** a rubber-band guitar on a tissue box: tight band high, loose band low.
8. **Debrief and patch: High Flyers.** "Can you sing the highest note you can? And the lowest?"

### Mission 4: Beat and Rhythm (pulse, rhythm, tempo)
1. **Problem:** "Feel your heart, or tap your feet when you walk. Can you feel a beat?"
2. **Move, everyone:** March to the beat. Then freeze dance: the music stops, you freeze.
3. **Story with sound:** Fizz the noise bot is the drummer: boom (big drum), tap (snare), tss (hi-hat).
4. **Toy, Co-pilot:** the Beat Pad: tap the big drum with the beat; it glows on every beat. No score.
5. **Guess:** "Tortoise speed or hare speed?" Two pieces of music.
6. **Big Question: The Speed Problem.** Moon Run needs music. Fast music is exciting but can feel rushed; slow music is calm but can feel sleepy. A) Fast like a hare. B) Slow like a tortoise. C) Start slow and get faster as you get near the flag. Hear each. Reveal: real games did all three; Space Invaders (1978) famously sped its four-note march up as the aliens came closer (research/01). The crew's choice sets the Moon Run speed.
7. **Make:** an eight-box drum beat with boom, tap and tss. Saved to the Beat slot.
8. **Try it at home:** a pots-and-pans drum kit with wooden spoons.
9. **Debrief and patch: Beat Keepers.** "What's your favourite speed to dance at?"

### Mission 5: Make a Tune (melody: pitch plus rhythm)
1. **Problem:** "When our robot reaches the flag, the game should play a winning tune. We need one!"
2. **Story with sound:** a tune is notes going up and down, long and short. Hear one you know (Twinkle Twinkle, a public-domain tune, played by Hoot).
3. **Guess:** "Does Twinkle Twinkle go up or down at the start?" (Up.)
4. **Echo game, everyone:** Bleep sings three notes on coloured pads, you copy them. Every answer gets a cheer; matching ones get a sparkle.
5. **Story with sound:** the five magic notes: these five always sound good together, so there are no wrong notes.
6. **Big Question: The Sharing Problem.** Two composers, one tune with eight boxes. How do we share? A) Take turns, one box each. B) One does the high notes, one does the low notes. C) One does the first half, one the second. D) Both tap at the same time. Reveal: real bands do all of these. Whatever you chose, let's try it now.
7. **Make:** the Song Maker in Tiny mode (eight boxes, five magic notes, big blocks) using the sharing rule the crew chose (the app shows whose turn it is if they chose A). Saved to the Win tune slot. Test in Moon Run.
8. **Debrief and patch: Tune Smiths.** "Hum your tune! What would you change?"

### Mission 6: Game Sounds Lab (sound effects and effects)
1. **Problem:** Moon Run: "Our robot jumps but makes no sound!"
2. **Story with sound:** every game sound is a recipe: a robot, a start note, a slide, and how long. Hear a laser (slides down), a jump (slides up), a coin (two quick notes), a crash (Fizz).
3. **Guess:** "A jump sound: does it slide up or slide down?" (Usually up.)
4. **Toy, Co-pilot:** the Silly Sound Machine: four big effect buttons: wobble, echo, slide, sparkle. Every tap makes a noise.
5. **Listening game, everyone:** Sound Detective: one person makes a sound with a recipe card, the others guess which card.
6. **Big Question: The Channel Problem.** The chip has four channels and the music is using all of them. You grab a star and the star sound needs a channel. A) Let the music go quiet for a moment while the star sound borrows its channel. B) No star sound; keep the music. C) Make the music use only three channels, so one is always free. Reveal: many NES games did A (listen closely and part of the music blinks out); some composers kept a channel free (research/01). Moon Run will do what the crew chose.
7. **Make:** design the jump in the Sound Lab (robot, start, slide, length, one effect). Saved to the Jump slot. Test in Moon Run.
8. **Debrief and patch: Sound Designers.** "What sound would a dragon's sneeze make?"

### Mission 7: Happy and Sad Chords (chord progressions)
1. **Problem:** "Listen to these two. Which sounds like a sunny day? Which sounds like a rainy day?"
2. **Guess, Co-pilot:** happy face or sad face, for each chord.
3. **Story with sound:** a chord is notes playing together. Old chips could only play a few notes at once, so composers played the chord's notes one after another, very fast: a sparkle (an arpeggio, research/01).
4. **Move:** sunny chord, big bouncy dance; rainy chord, slow sway.
5. **Toy:** Chord Blocks: Home, Sunny, Ready and Rainy blocks. Put four in a row and they loop. The magic-note pads play on top.
6. **Big Question: The Ending.** At the end of the game, the robot gets home, but says goodbye to its friend who stays on the Moon. Should the ending music be A) happy, B) a bit sad, or C) both at once? Hear each. Reveal: composers often mix happy and sad on purpose; some people call it bittersweet. There's no right answer: it depends on how you want people to feel.
7. **Make:** the crew's four-chord loop. Saved to the Chords slot; it backs the song in M8.
8. **Try it at home:** a water-glass xylophone (plastic cups or jars, a grown-up pours, tap with a spoon).
9. **Debrief and patch: Chord Crew.** "Which chord feels like you today?"

### Mission 8: Our Game, Our Song (the capstone, with a tracker)
1. **Problem:** "Moon Run has a bump, a star, a jump and a winning tune. But no music! Let's write its song."
2. **Story:** real chiptune composers wrote songs in a **tracker**: the song goes down the screen like a ladder, one row at a time. Some musicians still make music on old Game Boys today (research/01). Show the Song Maker's Tracker view.
3. **Plan:** the four channels are the band: Bleep (tune), Sparkle (chords), Hoot (bass) and Fizz (drums). Who plays the tune? The Commander chooses the tune robot.
4. **Make, part one:** the Song Maker in Big mode, starting from the crew's Beat and Chords. Commander does the tune, Co-pilot adds drums and presses PLAY.
5. **Rule change (Synthesis):** "News from the game designer: the last part of Moon Run is harder. Can the music get faster there?" The crew adds a second page and makes it faster, or decides not to, and says why.
6. **Make, part two:** name the song, choose a cartridge colour and sticker, save to the Jukebox and set it as the Moon Run music.
7. **Play Moon Run:** everything the crew made, all at once.
8. **Debrief and patch: Chiptune Composers** (gold). "What worked? What would you change next time?" and "Who should we play our game to?"

### The Studio (free play, always open)
- **Song Maker.** Tiny mode (8 boxes, 5 magic notes, one drum row, huge blocks: the Co-pilot) and Big mode (16 boxes a page, up to four pages, 8 notes in magic or all-notes scale, three drum rows, a chord row, long notes, robot choice, speed animals, channel mute buttons, a Tracker view). Save as a cartridge to the Jukebox.
- **Bleep Pads.** Eight huge rainbow pads in magic notes, robot picker, wobble and echo switches, a big LCD wave. Made for the Co-pilot.
- **Sound Lab.** The sound-effect recipe maker with preset cards (jump, coin, laser, power-up, crash), and a small "recipe" line for Dad.
- **Wave Drawer.** Draw a 32-step wave and play it on pads.
- **Chord Blocks.** The four-chord looper with pads on top.
- **Jukebox.** Saved songs as cartridges, plus demo songs: Twinkle Twinkle, Frère Jacques, Ode to Joy (all public domain) and two original tunes, Moon Run Theme and Robot Dance.
- **Moon Run.** The game.

---

## 5. Gamification that stays collaborative

- **Patches.** One per mission, retro-cartridge style, with all three names.
- **Changed-Mind stars.** Any crew member who changes their vote after hearing the others earns a star. The only counter the app celebrates out loud.
- **Crew Log.** Every guess, vote, "why" line and made thing, dated. Dad can export it.
- **The Moon Run cartridge.** Slots light up as the crew fills them.
- **No locks, timers, streaks, points or scores between the children.**

---

## 6. Look and feel

- **Landscape tablet first**, designed at 1280 by 800 CSS px, working from 1024 to 1600 wide, usable in portrait.
- **A stylish handheld console, not a cartoon.** Warm off-white console body, chunky coloured buttons, dark green four-shade LCD panels (the original Game Boy palette) for waves, the tracker and the game. Flat, bold colour coding: each robot has one colour everywhere; notes use the classroom Boomwhacker rainbow (C red, D orange, E yellow, F lime, G green, A purple, B pink).
- **Type:** Lexend for everything a child hears or reads (as Astra Maths), a pixel display face (Press Start 2P, Google Fonts) only for short labels like PLAY and the logo.
- **Size:** Co-pilot tap targets at least 96 px (big pads and the Tiny Song Maker are bigger), everything else at least 64 px, body text at least 22 px. No double-tap, no long-press, no gesture a three-year-old can't do; drag is optional everywhere (tapping works too).
- **Sound on by default** (it is a music app), with a volume control. Every touch makes a sound within about 50 ms: pads trigger on pointer-down.
- **Read aloud:** UK English voice, automatic, with a repeat button on every card and an off switch.

---

## 7. Technical architecture (zero build step)

Plain static site, the same family as the sister apps.

```
index.html, manifest.webmanifest, sw.js (generated)
css/app.css
js/app.js                 boot, router, home, setup, notes, log
js/core/                  dom, store, speak, ui, icons, theme, patch, bots (SVG robots)
js/core/chip.js           the sound chip: voices, drums, effects, scope tap
js/core/seq.js            look-ahead sequencer for songs and loops
js/core/song.js           song model, scales, chords, demo songs, Moon Run sound kit
js/core/runner.js         mission runner and step types
js/toys/                  one module per interactive toy (Song Maker, pads, lab, drawer, chords, games)
js/game/moonrun.js        the game
content/missions.json     mission list
content/missions/*.json   one file per mission
research/                 facts, teaching, videos
tools/                    build_sw.py, publish.py, shot.sh, make_icons.py
dev/                      harness.html (mount any toy), smoke.html (every mission), audio-test.html
```

- **Toy interface** (as Astra Maths widgets): `mount(el, props, api)` returns `{ destroy(), getState?() }`. `api` gives `done()`, `say(text)`, `log(text)`, `crew`, `kit` (read and write the Moon Run sound kit). Toys never touch the router.
- **Audio:** Web Audio API only, created on the first touch (Android needs a gesture). Voices are `PeriodicWave`s computed from 32 or 64-step tables: pulse at 12.5, 25 and 50 percent, a 4-bit stepped triangle like the NES, a sawtooth, and any drawn wave. Noise is a 15-bit LFSR buffer like the NES (long and short modes). Effects: wobble (vibrato LFO), slide (frequency ramp), sparkle (arpeggio at tracker speed), echo (a feedback delay bus). A compressor on the master so a crew tapping eight pads never clips. An analyser feeds the LCD scopes.
- **Sequencer:** look-ahead scheduling (a 25 ms timer schedules notes 120 ms ahead on the audio clock) with a visual playhead from `requestAnimationFrame`. Four channels: lead, chords, bass, drums. Sound effects in Moon Run can borrow the lead channel (the M6 Big Question).
- **Storage:** `localStorage` key `astrableeps.v1`: crew, patches, stars, log, settings, the sound kit, saved songs (as compact JSON). No backend, no analytics, no microphone.
- **Offline:** `tools/build_sw.py` writes `sw.js` with a precache list and a content-hash version, copied from the sister app. Fonts are cached at runtime.
- **Deploy:** `python tools/publish.py "C:/1 Astra Nova - Finn/bleeps"`, then commit and push the Astra Finn repo. The Astra Finn service worker must ignore `/bleeps/` as it ignores `/maths/`.

---

## 8. Content rules

- One to three short sentences per card, under twelve words a line where possible. Every card is read aloud and has a repeat button.
- One number per card, always with a comparison a six-year-old can picture, and a `source` URL from `research/01`.
- Describe sounds with child words first (beepy, soft, buzzy, hissy, high, low, fast, slow, long, short), the real word second ("that's called a square wave").
- Never "wrong". A missed guess gets "Ooh, good guess! Listen..." and the sound again.
- Big Questions (M4, M5, M6, M7 only): three or four picture options, a sound preview where it helps, no right answer, a reveal that says what real composers did without crowning an option. Written so a crew could split.
- Every mission ends with a debrief ("What was your favourite part?" plus one question) and a patch.
- No scary content, no violence. Old tunes used are public domain (Twinkle Twinkle, Frère Jacques, Ode to Joy). No copyrighted game music is reproduced; game history is told in words.
- Steps meant for the three-year-old carry `"who": "copilot"`; the runner shows the Co-pilot badge and reads the Co-pilot's name.

---

## 9. Engineer's notes (for Dad)

A crib page behind a button: how a session runs, which steps are the Co-pilot's, what each mission teaches mapped to the original course goals (waveforms; melodies with pitch and rhythm; chord progressions; sound effects; the tracker) and to England's EYFS and Key Stage 1 music words (research/02), a glossary (chiptune, channel, square and pulse width, triangle, sawtooth, noise, arpeggio, vibrato, tracker, tempo, pentatonic, major and minor, chord progression), the facts with sources, the Crew Log export, and reset.

---

## 10. Testing

- `dev/harness.html?toy=<name>` mounts any toy on its own; `dev/smoke.html` walks every step of every mission and reports errors; `dev/audio-test.html` plays every voice, drum and effect.
- `tools/shot.sh <name> "<path>"` takes headless Chrome screenshots on port 8100 and prints console lines. `?devcrew` skips crew setup.
- Real-browser checks in the built-in browser pane at 1280 by 800 and 1024 by 768, with sound.
- Offline: headless Edge and `dev/test-sw.html` (headless Chrome on this PC fails service-worker cache writes).

---

## 11. Build order and delegation

**Haiku 5.5, in parallel, research only (started first):**
1. `research/01-chiptune-facts.md`: consoles, chips, channels, dates, sales, Space Invaders, trackers, arpeggios, sound science, with URLs.
2. `assets/img/` and `CREDITS.md`: public-domain photos of the Game Boy, NES, Famicom, Commodore 64, the SID chip, a speaker, a tuning fork.
3. `research/02-teaching-young-children.md`: EYFS, KS1, Model Music Curriculum, what 3 and 6-year-olds can do, kitchen experiments, touch targets.
4. `research/03-videos.md`: a few verified, family-friendly videos (sound for kids, a real Game Boy being played).

**Opus 5.5 builds, in this order:**
1. Core: store, speech, UI, icons, theme, bots, the sound chip and the sequencer, `dev/audio-test.html`.
2. The Studio: Song Maker (Tiny and Big, tracker view), Bleep Pads, Jukebox with demo songs.
3. The runner, step types (story, guess, Big Question, toy, move, at-home, make, game, video, finish), home, crew setup, notes, log.
4. Toys for the missions: wake the bots, close-your-eyes, Wave Drawer, pulse width, Pitch Ladder and Lift game, Beat Pad and freeze dance, Echo game, Silly Sound Machine, Sound Lab, Chord Blocks, the make steps.
5. Moon Run.
6. The eight missions' content, written from the research files.
7. PWA plumbing, icons, publish into the Astra Finn repo.

**Done means:** installed from the public link on the tablet, Mission 1 and the Song Maker finished end to end with sound and no console errors, Moon Run playing the crew's sounds, and the app still opening with Wi-Fi off after one online visit.
