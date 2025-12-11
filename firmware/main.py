# You import all the IOs of your board
import board
import neopixel

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.modules.rotary_encoder import RotaryEncoderHandler
from kmk.extensions.RGB import RGB

#These are my leds
rgb = RGB(pixel_pin=board.GP26, num_pixels=4)
keyboard.extensions.append(rgb)


# This is the main instance of your keyboard
keyboard = KMKKeyboard()

# Add the macro extension
macros = Macros()
keyboard.modules.append(macros)

# Define your pins here!
PINS = [board.GP27, board.GP28, board.GP29, board.GP6, board.GP7, board.GP00, board.GP4, board.GP2, board.GP1]

encoder_handler = RotaryEncoderHandler()
keyboard.modules.append(encoder_handler)


encoder_handler.pins = (board.GP1, board.GP2)
encoder_handler.divisor = 4
encoder_handler.map = [KC.VOLD, KC.VOLU] 
# Tell kmk we are not using a key matrix
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# Here you define the buttons corresponding to the pins
# Look here for keycodes: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
# And here for macros: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macrosu.md
keyboard.keymap = [
    [KC.W, KC.A, KC.S, KC.D, KC.DEL, KC.SPC, KC.RGB_MODE_RAINBOW]
]

# Start kmk!
if __name__ == '__main__':
    keyboard.go()