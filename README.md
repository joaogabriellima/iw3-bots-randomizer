# MW3 Bot Nickname Randomizer

This is a simple Python script that personalizes bot names in **Call of Duty: Modern Warfare 3 (Plutonium Mod)** by randomizing 18 unique nicknames every time you run it. Adds variety and immersion to solo matches!

> Made for the OGs still playing MW3 even after their squad moved on.


## What does it do?

1. Loads a `names.json` file containing dozens of custom nicknames.
2. Randomly picks **18 unique names**.
3. Generates a new `bots.txt` file.
4. Injects it into the `z_svr_bots.iwd` file used by the Plutonium mod (a renamed ZIP archive).
5. That’s it — new bot names every time you launch the game.


## How to Use

### 1. Requirements

- Python 3 installed → [https://www.python.org/downloads/](https://www.python.org/downloads/)
- Plutonium MW3 installed with [iw3_bot_warfare](https://github.com/ineedbots/iw3_bot_warfare)

### 2. Configure your `.iwd` file path

In `bots.py`, edit this line to point to your actual `z_svr_bots.iwd` file:

```python
IWD_PATH = "C:\\Users\\YourUser\\AppData\\Local\\Plutonium\\storage\\iw5\\z_svr_bots.iwd"
```

## File sample
```
[
    "MrVolps",
    "ohDooM_",
    "Zz_NeVeR_FoRGeTZ",
    "The_MVPereira",
    "zHiiTz__",
    "FxB_Playjoa",
    "FxB_DollyRivals",
    "Fxb_Profetz",
    "Zz_Fat_Zz",
    "TeForzz"
]
```

## Credits

- [Plutonium](https://plutonium.pw/)
- [iw3 bot warfare](https://github.com/ineedbots/iw3_bot_warfare)
