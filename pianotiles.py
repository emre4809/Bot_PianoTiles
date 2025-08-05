import mss
from PIL import Image
import keyboard
import time

# Constants for the screenshot area
# Adjust these values based on your screen resolution and the game window position
# These values are for a 1920x1080 screen, adjust accordingly if your resolution is different
SCT_TOP = 910
SCT_LEFT = 825
SCT_WIDTH = 550
SCT_HEIGHT = 1


class Screenshot:
    """    
    This class handles the screenshot capturing logic.
    It captures a specific area of the screen and returns it as a grayscale image
    """
    def __init__(self):
        pass

    def capture(self):
        """
        Takes a screenshot of the defined area and returns a grayscale PIL Image
        """
        monitor = {
            "left": SCT_LEFT,
            "top": SCT_TOP,
            "width": SCT_WIDTH,
            "height": SCT_HEIGHT
        }
        with mss.mss() as sct:
            sct_img = sct.grab(monitor)
            img = Image.frombytes("RGB", sct_img.size, sct_img.rgb)
            bw_img = img.convert("L")  # Convert to grayscale
            return bw_img


class Clicker:
    """
    This class will handle the clicking logic
    """
    keys = ["q", "w", "e", "r"] # Defined keys for each column in BlueStacks. For ex. when q is pressed, the tile in the first column is clicked.

    def __init__(self):
        pass

    def click_tiles(self, img):
        """
        Checks each column for black pixels and presses the corresponding key
        """
        pixels = img.load()
        column_width = SCT_WIDTH // 4
        for i in range(4):
            # Check the center pixel of each column
            x = i * column_width + column_width // 2 # x is the center of the column
            y = 0  # Only one row since height is 1
            if pixels[x, y] < 20:  # Threshold for black (0 is black)
                keyboard.press_and_release(self.keys[i])


def main():
    screenshot = Screenshot()
    clicker = Clicker()
    print("Piano Tiles bot started. Press ESC to stop.")
    try:
        while True:
            if keyboard.is_pressed("esc"):
                print("ESC pressed. Bot stopped.")
                break
            img = screenshot.capture()
            clicker.click_tiles(img)
            time.sleep(0.1)  # ~10 checks per second, can be adjusted to more checks per second
    except Exception as e:
        print(f"{e}")


if __name__ == "__main__":
    main()