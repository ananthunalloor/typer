# Title: KMK Firmware for Typer ONE Keyboard
import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

from kmk.modules.split import Split,SplitType
# from kmk.modules.split import SplitSide

keyboard = KMKKeyboard()

split = Split(split_side=None, split_type=SplitType.UART, data_pin=board.GP0, data_pin2=board.GP1, use_pio=True, uart_flip=True )
keyboard.modules.append(split)

keyboard.col_pins = (board.GP2,board.GP3, board.GP4, board.GP5, board.GP6, board.GP7, board.GP8, board.GP9)
keyboard.row_pins = (board.GP14,board.GP15,board.GP26,board.GP27,board.GP28)
keyboard.diode_orientation = DiodeOrientation.COLUMNS

L1_SPC = KC.LT(1, KC.SPC)
L2_ENT = KC.LT(2, KC.ENT)
S_BSPC = KC.HT(KC.BSPC, KC.LSFT)
C_DEL = KC.HT(KC.DEL, KC.LCTL)
M_END = KC.HT(KC.END, KC.MEH)
H_PGDN = KC.HT(KC.PGDN, KC.HYPER)

#ergodox keymap
keyboard.keymap = [
    # left hand base layer
        [   #0
        KC.ESC,    KC.N1,  KC.N2,   KC.N3,   KC.N4,  KC.N5, KC.DEL,
        KC.TAB,     KC.Q,   KC.W,    KC.E,    KC.R,   KC.T, KC.BSPC,
        KC.CAPS,    KC.A,   KC.S,    KC.D,    KC.F,   KC.G, KC.ENT, KC.LGUI,
        KC.LSFT,    KC.Z,   KC.X,    KC.C,    KC.V,   KC.B, KC.LALT, KC.HOME,
        KC.LCTL, KC.MINS, KC.EQL, KC.LEFT, KC.RGHT,   L1_SPC,  S_BSPC, M_END
    ],

]

keyboard.coord_mapping = [
    0, 1, 2, 3, 4, 5, 6,
    7, 8, 9, 10, 11, 12, 13,
    14, 15, 16, 17, 18, 19, 20,
    21, 22, 23, 24, 25, 26, 27,
    28, 29, 30, 31, 32, 33, 34,35, 36, 37
]

if __name__ == '__main__':
    keyboard.go()

"""
# TESTING AREA




# END TESTING AREA
"""