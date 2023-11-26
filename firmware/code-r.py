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

keyboard.col_pins = (board.GP2,board.GP3, board.GP4, board.GP5, board.GP6, board.GP7, board.GP8)
keyboard.row_pins = (board.GP14,board.GP15,board.GP16,board.GP17,board.GP18)
keyboard.diode_orientation = DiodeOrientation.COLUMNS

L1_SPC = KC.LT(1, KC.SPC)
L2_ENT = KC.LT(2, KC.ENT)
S_BSPC = KC.HT(KC.BSPC, KC.LSFT)
C_DEL = KC.HT(KC.DEL, KC.LCTL)
M_END = KC.HT(KC.END, KC.MEH)
H_PGDN = KC.HT(KC.PGDN, KC.HYPER)

keyboard.keymap = [
    [   #0
        KC.ESC,    KC.N1,  KC.N2,   KC.N3,   KC.N4,  KC.N5,                                         KC.N6, KC.N7,   KC.N8,   KC.N9,   KC.N0,  KC.GRV,
        KC.TAB,     KC.Q,   KC.W,    KC.E,    KC.R,   KC.T,                                          KC.Y,  KC.U,    KC.I,    KC.O,    KC.P, KC.BSLS,
        KC.CAPS,    KC.A,   KC.S,    KC.D,    KC.F,   KC.G,                                          KC.H,  KC.J,    KC.K,    KC.L, KC.SCLN, KC.QUOT,
        KC.LSFT,    KC.Z,   KC.X,    KC.C,    KC.V,   KC.B, KC.LALT, KC.LGUI,    KC.RGUI, KC.RALT,   KC.N,  KC.M, KC.COMM,  KC.DOT, KC.SLSH, KC.RSFT,
        KC.LCTL, KC.MINS, KC.EQL, KC.LEFT, KC.RGHT,                  KC.HOME,    KC.PGUP,           KC.UP, KC.DOWN, KC.LBRC, KC.RBRC, KC.RCTL,
                                                    L1_SPC,  S_BSPC,   M_END,     H_PGDN,   C_DEL, L2_ENT
    ],
    [   #1
        KC.F1,     KC.F2,  KC.F3,   KC.F4,   KC.F5,   KC.F6,                                      KC.F7,   KC.F8, KC.F9,  KC.F10,  KC.F11,  KC.F12,
        KC.NO,     KC.NO,  KC.NO,   KC.NO,   KC.NO,   KC.NO,                                      KC.NO,   KC.P7, KC.P8,   KC.P9, KC.PMNS,   KC.NO,
        KC.NLCK, KC.SLCK, KC.INS, KC.PAUS, KC.PSCR,   KC.NO,                                    KC.PAST,   KC.P4, KC.P5,   KC.P6, KC.PPLS,   KC.NO,
        KC.TRNS,   KC.NO,  KC.NO,   KC.NO,   KC.NO,   KC.NO, KC.NO, KC.NO,    KC.TRNS, KC.TRNS, KC.PSLS,   KC.P1, KC.P2,   KC.P3, KC.PEQL, KC.TRNS,
        KC.TRNS,   KC.NO,  KC.NO,   KC.NO,   KC.NO,                 KC.NO,    KC.TRNS,                   KC.PCMM, KC.P0, KC.PDOT,   KC.NO, KC.TRNS,
                                                    KC.TRNS, KC.NO, KC.NO,    KC.TRNS, KC.TRNS, KC.PENT
    ],
    [   #2
        KC.F13,   KC.F14, KC.F15, KC.F16,   KC.F17,  KC.F18,                                     KC.F19,   KC.F20,   KC.F21, KC.F22, KC.F23,    KC.F24,
        KC.NO,     KC.NO,  KC.NO,  KC.NO,  KC.VOLU,   KC.NO,                                      KC.NO,     KC.NO,   KC.NO,  KC.NO,  KC.NO,     KC.NO,
        KC.RESET,  KC.NO,  KC.NO,  KC.NO,  KC.MUTE,   KC.NO,                                      KC.NO, KC.BT_NXT, KC.BRIU,  KC.NO,  KC.NO,  KC.DEBUG,
        KC.NO,     KC.NO,  KC.NO,  KC.NO,  KC.VOLD,   KC.NO, KC.TRNS, KC.TRNS,    KC.NO, KC.NO,   KC.NO, KC.BT_PRV, KC.BRID,  KC.NO,  KC.NO,     KC.NO,
        KC.RLD,    KC.NO,  KC.NO,  KC.NO,    KC.NO,                   KC.TRNS,    KC.NO,                     KC.NO,   KC.NO,  KC.NO,  KC.NO, KC.BT_CLR,
                                                    KC.MPLY, KC.TRNS, KC.TRNS,    KC.NO, KC.NO, KC.TRNS
    ]
]

coord_mapping = [
    0, 1, 2, 3, 4, 5, 6,
    7, 8, 9, 10, 11, 12, 13,
    14, 15, 16, 17, 18, 19, 20,
    21, 22, 23, 24, 25, 26, 27,
]

if __name__ == '__main__':
    keyboard.go()

#TESTING