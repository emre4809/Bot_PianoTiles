# Bot_PianoTiles

This is a short project I created to learn about Python automation and screen interaction. The bot automatically plays the Piano Tiles game on BlueStacks by detecting black tiles in four columns and pressing the corresponding keys.

## How It Works

- The bot takes rapid screenshots of a specific area of your screen where the game columns are located.
- It analyzes the pixels in each column to detect black tiles.
- When a black tile is detected, it simulates a key press ("q", "w", "e", "r") to "click" the tile in the game.

## Setup

1. **Download and install BlueStacks.**
2. **Clone the repository:**

   git clone https://github.com/emre4809/Bot_PianoTiles.git

3. **Install dependencies:**

  Written in requirements.txt

4. **Adjust screenshot area:**

   Edit `SCT_TOP`, `SCT_LEFT`, `SCT_WIDTH`, and `SCT_HEIGHT` in `pianotiles.py` to match your BlueStacks window and screen resolution.

6. **Run the bot:**
   ```
   python pianotiles.py
   ```
   To stop the bot: `ESC`

## Notes

- This project is for educational purposes and personal learning.
- Make sure to run the bot only on your own system and respect the terms of service of any software you use it with.
- You may need to further calibrate the screenshot area and pixel threshold for your setup.
- **Tested with:** Piano Tiles 2 and Piano Music Tiles on BlueStacks.
