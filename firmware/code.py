# Title: KMK Firmware for Typer ONE Keyboard
import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

from kmk.modules.split import Split, SplitType
# from kmk.modules.split import SplitSide

keyboard = KMKKeyboard()

split = Split(split_side=None, split_type=SplitType.UART,
              data_pin=board.GP0, data_pin2=board.GP1, use_pio=True, uart_flip=True)
keyboard.modules.append(split)

keyboard.col_pins = (board.GP2, board.GP3, board.GP4,
                     board.GP5, board.GP6, board.GP7, board.GP8, board.GP9)
keyboard.row_pins = (board.GP14, board.GP15,
                     board.GP26, board.GP27, board.GP28)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# add debug
# keyboard.debug_enabled = True

# key mapping
keyboard.coord_mapping = [
    0,  1,  2,  3,  4,  5,  6,  7,   47, 46, 45, 44, 43, 42, 41, 40,
    8,  9,  10, 11, 12, 13, 14, 15,  55, 54, 53, 52, 51, 50, 49, 48,
    16, 17, 18, 19, 20, 21, 22, 23,  63, 62, 61, 60, 59, 58, 57, 56,
    24, 25, 26, 27, 28, 29, 30, 31,  71, 70, 69, 68, 67, 66, 65, 64,
    32, 33, 34, 35, 36, 37, 38, 39,  79, 78, 77, 76, 75, 74, 73, 72
]

# ergodox keymap
keyboard.keymap = [
    # base layer
    [   # Left layer                                                               #Right layer
        KC.ESC,  KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,  KC.MINS, KC.NO,       KC.NO,   KC.EQL,  KC.N6,  KC.N7, KC.N8,    KC.N9,   KC.N0,   KC.GRAVE,
        KC.TAB,  KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,   KC.HYPR, KC.NO,       KC.NO,   KC.MEH,  KC.Y,   KC.U,  KC.I,     KC.O,    KC.P,    KC.BSLS,
        KC.CAPS, KC.A,    KC.S,    KC.D,    KC.F,    KC.G,   KC.LT,   KC.PGUP,     KC.PGDN, KC.LT,   KC.H,   KC.J,  KC.K,     KC.L,    KC.SCLN, KC.QUOT,
        KC.LSFT, KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,   KC.HOME, KC.INS,      KC.PSCR, KC.END,  KC.N,   KC.M,  KC.COMMA, KC.DOT,  KC.SLSH, KC.RSHIFT,
        KC.LCTL, KC.LBRC, KC.LALT, KC.LEFT, KC.RGHT, KC.SPC, KC.LSFT, KC.HOME,     KC.DEL,  KC.BSPC, KC.ENT, KC.UP, KC.DOWN,  KC.LALT, KC.RBRC, KC.RCTRL
    ],

    # fn layer
    [   # Left layer                                                               #Right layer
        KC.NO,   KC.F1,   KC.F2,   KC.F3,   KC.F4,   KC.F5,  KC.F6,   KC.NO,       KC.NO,   KC.F7,   KC.F8,   KC.F9,   KC.F10,  KC.F11,  KC.F12,  KC.NO,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,KC.TRNS, KC.NO,       KC.NO,   KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,KC.TRNS, KC.TRNS,     KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,KC.TRNS, KC.TRNS,     KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,KC.TRNS, KC.TRNS,     KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS
    ],

    # media layer
    [   # Left layer                                                               #Right layer
        KC.NO,   KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,KC.TRNS, KC.NO,       KC.NO,   KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.NO,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,KC.TRNS, KC.NO,       KC.NO,   KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,KC.TRNS, KC.TRNS,     KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,KC.TRNS, KC.TRNS,     KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,KC.TRNS, KC.TRNS,     KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS
    ]
]

if __name__ == '__main__':
    keyboard.go()