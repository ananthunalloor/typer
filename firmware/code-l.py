# Title: KMK Firmware for Typer ONE Keyboard

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

from kmk.modules.split import Split, SplitSide, SplitType

keyboard = KMKKeyboard()

split = Split(split_side=SplitSide.LEFT, split_type=SplitType.UART, data_pin=board.GP0, data_pin2=board.GP1, use_pio=True, uart_flip=True )
keyboard.modules.append(split)

keyboard.col_pins = (board.GP2,board.GP3)
keyboard.row_pins = (board.GP14,board.GP15,board.GP16,board.GP17,board.GP18)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [
        KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P
    
    ],
    [
        KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.ENT
    
    ],
    [
        KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.ESC, KC.SPACE, KC.BSPC
    ]
]

if __name__ == '__main__':
    keyboard.go()

#TESTING