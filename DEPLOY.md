# Getting Astra Bleeps onto the tablet

## Where it lives

Astra Bleeps is published inside the Astra Finn GitHub Pages site, in its own folder, so it has its own address, its own home-screen icon and its own offline copy:

**https://philhandley.github.io/astra-finn/bleeps/**

The source of truth is this folder (`C:\1. Astra Bleeps - Chiptunes`, its own git repository). Publishing copies the app files into `C:\1 Astra Nova - Finn\bleeps\` and pushes that repository.

## Updating it after a change

From this folder:

```bash
python tools/build_sw.py
```

```bash
python tools/publish.py "C:/1 Astra Nova - Finn/bleeps"
```

Then in `C:\1 Astra Nova - Finn`:

```bash
git add bleeps && git commit -m "Update Astra Bleeps" && git push
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
