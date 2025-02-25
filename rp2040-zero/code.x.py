"""CircuitPython status NeoPixel red, green, blue example."""
import time
import board
from digitalio import DigitalInOut, Direction, Pull
import neopixel


led = DigitalInOut(board.GP29)
led.direction = Direction.OUTPUT


'''
#pin.value(0)
pin.value(1)
#pin.value(True)
pin.value(False)
pin.high()
#pin.low()
'''

pixel = neopixel.NeoPixel(board.NEOPIXEL, 1)

pixel.brightness = 0.1

while True:
    
    led.value = True
    pixel.fill((64, 0, 0))
    time.sleep(0.5)
    pixel.fill((0, 64, 0))
    time.sleep(0.5)
    led.value = False
    pixel.fill((0, 0, 64))
    time.sleep(0.5)