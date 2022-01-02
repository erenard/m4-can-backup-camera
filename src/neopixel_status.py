import board
import neopixel

def setup():
    global pixels
    pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)

def standby():
    pixels[0] = (0, 0, 0)

def reversing():
    pixels[0] = (5, 5, 5)
