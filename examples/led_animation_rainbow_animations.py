# SPDX-FileCopyrightText: 2021 Kattni Rembor for Adafruit Industries
# SPDX-License-Identifier: MIT

"""
This example uses AnimationsSequence to display multiple animations in sequence, at a five second
interval.

For NeoPixel FeatherWing. Update pixel_pin and pixel_num to match your wiring if using
a different form of NeoPixels.

This example does not work on SAMD21 (M0) boards.
"""
import board
from led_simulation import LEDSimulation
from animation.rainbow import Rainbow
from animation.rainbowchase import RainbowChase
from animation.rainbowcomet import RainbowComet
from animation.rainbowsparkle import RainbowSparkle
from sequence import AnimationSequence

# Defintions
pixel_num = 30
display = board.DISPLAY

# Create a LEDSimulation object
pixels = LEDSimulation(
    display, led_count=30, led_spacing=9, led_radius=4, led_color=0x000000
)


rainbow_chase = RainbowChase(pixels, speed=0.1, size=5, spacing=3)
rainbow_comet = RainbowComet(pixels, speed=0.1, tail_length=7, bounce=True)

animations = AnimationSequence(
    rainbow_chase,
    rainbow_comet,
    advance_interval=5,
    auto_clear=True,
)

while True:
    animations.animate()
