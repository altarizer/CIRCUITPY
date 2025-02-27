import board
import time
from digitalio import DigitalInOut, Direction, Pull
import random

R = DigitalInOut(board.GP26)
R.direction = Direction.OUTPUT
G = DigitalInOut(board.GP27)
G.direction = Direction.OUTPUT
B = DigitalInOut(board.GP28)
B.direction = Direction.OUTPUT

"""
R.value = True
G.value = False
B.value = True

D0 = DigitalInOut(board.GP5)
D0.direction = Direction.OUTPUT
D1 = DigitalInOut(board.GP6)
D1.direction = Direction.OUTPUT
D2 = DigitalInOut(board.GP7)
D2.direction = Direction.OUTPUT
D3 = DigitalInOut(board.GP8)
D3.direction = Direction.OUTPUT
D4 = DigitalInOut(board.GP9)
D4.direction = Direction.OUTPUT
D5 = DigitalInOut(board.GP10)
D5.direction = Direction.OUTPUT
D6 = DigitalInOut(board.GP11)
D6.direction = Direction.OUTPUT
D7 = DigitalInOut(board.GP12)
D7.direction = Direction.OUTPUT
"""

while True:        
    R.value = random.choice([True, False])
    G.value = random.choice([True, False])
    B.value = random.choice([True, False])
    time.sleep(2.0) 


