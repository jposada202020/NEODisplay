# SPDX-FileCopyrightText: 2021 Kattni Rembor for Adafruit Industries
# SPDX-License-Identifier: MIT

"""
Example of the Comet animation using the LEDSimulation Library.
"""
import board
from animation.comet import Comet
from color import JADE, BLUE
from led_simulation import LEDSimulation


# Defintions
pixel_num = 30
display = board.DISPLAY

# Create a LEDSimulation object
pixels = LEDSimulation(
    display, led_count=30, led_spacing=9, led_radius=4, led_color=0x000000
)

comet = Comet(pixels, speed=0.1, color=BLUE, tail_length=10, bounce=True)

while True:
    comet.animate()
