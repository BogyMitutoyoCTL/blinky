#!/usr/bin/python3

from time import sleep
from luma.core.render import canvas
from luma.led_matrix.device import ws2812
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text
from luma.core.legacy.font import LCD_FONT, proportional
from luma.led_matrix.device import max7219
from time import sleep

'''
Pin connections:
VCC (red): 5 Volt, don't use Raspberry's power, because it may draw a lot of current
DIN (green): Pin 12, GPIO18
GND (white): Common ground
'''


def ws2812draw():
    device = ws2812(width=10, height=20, rotate=0)
    device.contrast(255)

    with canvas(device) as draw:
        draw.rectangle(device.bounding_box, outline="green", fill="blue")
        draw.line((0, 0, 8, device.height), fill="red")
        draw.line((1, 0, 1, device.height), fill="orange")
        draw.line((0, 0, 0, 0), fill="white")
        draw.line((0, 7, 0, 7), fill="white")
    sleep(3)
    for c in range(0, 255, 8):
        device.contrast(c)
        sleep(0.2)
    sleep(3)
    device.cleanup()
    del device


def matrix():

    serial = spi(port=0, device=0, gpio=noop())
    scoreboard = max7219(serial, cascaded=4, block_orientation=-90, rotate=2)
    virtual = viewport(scoreboard, width=200, height=8)
    scoreboard.contrast(20)
    with canvas(virtual) as draw:
        text(draw, (0, 0), "        BOGY 2019 - Mitutoyo CTL", fill="white", font=proportional(LCD_FONT))
    return virtual


def ws2812linear(width: int, height: int, rotate: int, virtual: viewport, mapping=None):
    device = ws2812(width=width, height=height, rotate=rotate, mapping=mapping)
    device.contrast(255)
    pos = 0
    while (True):
        pos = ChangeColor(device, height, pos, virtual, width, "blue")
        pos = ChangeColor(device, height, pos, virtual, width, "#00007F")
        pos = ChangeColor(device, height, pos, virtual, width, "red")
        pos = ChangeColor(device, height, pos, virtual, width, "yellow")
        pos = ChangeColor(device, height, pos, virtual, width, "violet")
        pos = ChangeColor(device, height, pos, virtual, width, "orange")
        pos = ChangeColor(device, height, pos, virtual, width, "green")
    sleep(3)
    device.cleanup()
    del device


def ChangeColor(device, height, pos, virtual, width, fillcolor):
    virtual.set_position((pos, 0))
    pos = pos + 1
    if pos > (virtual.width - 32):
        pos = 0
    with canvas(device) as draw:
        for w in range(width):
            for h in range(height):
                draw.point((w, h), fill=fillcolor)
    sleep(0.1)
    return pos


def ws2812linear2(width: int, height: int, rotate: int, mapping=None):
    device = ws2812(width=width, height=height, rotate=rotate, mapping=mapping)
    device.contrast(255)
    with canvas(device) as draw:
        for w in range(0, width, 2):
            for h in range(height):
                draw.point((w, h), fill="blue")
                draw.point((w + 1, h), fill="red")
    sleep(300)
    device.cleanup()
    del device


virtual = matrix()
ws2812linear(20, 10, 0, virtual)
print("end.")
