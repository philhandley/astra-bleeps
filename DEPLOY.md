# Getting Astra Bleeps onto the tablet

## Where it lives

**https://philhandley.github.io/astra-bleeps/**

This folder (`C:\1. Astra Bleeps - Chiptunes`) is the GitHub repository `philhandley/astra-bleeps`, published by GitHub Pages from `main`. It has its own address outside Astra Finn, so the tablet installs it as its own app. (It briefly lived at `/astra-finn/bleeps/`, which now redirects here.)

## Updating it after a change

```bash
python tools/build_sw.py
```

```bash
git add -A && git commit -m "Update Astra Bleeps" && git push
```

GitHub Pages redeploys in about two minutes.

## Installing on the Samsung tablet

**Samsung Internet:** open the address, tap the menu (three lines, bottom right), then **Add page to**, then **Home screen**. If an **Install** icon appears in the address bar, tap that instead.

**Chrome:** open the address, tap the three-dot menu, then **Add to Home screen**, then **Install**.

Then:
- Open it once on Wi-Fi and tap into a mission, so everything is saved for offline use. After that it works with Wi-Fi off (only the "Watch together" videos in the Engineer's notes need the internet).
- Turn the tablet sideways. It is designed for landscape.
- **Turn the media volume up** and make sure the tablet isn't on silent or Do Not Disturb: this is a music app. The volume slider at the bottom of the home screen sets how loud the robots are.
- The speaker button at the top switches automatic reading aloud on and off.

## First session (about 15 minutes)

1. Type the crew names: Finn as Commander, the little one as Co-pilot, Dad as Sound Engineer.
2. Let the Co-pilot tap the robots on the home screen for a minute. Each one sings.
3. Play **Mission 1: The Silent Game**. It ends with the crew choosing Moon Run's first sound.
4. If there's energy left, open the **Song Maker** in Tiny mode together, or the **Bleep Pads**.

Each later mission adds one more sound to Moon Run. Mission 8 writes its music.
