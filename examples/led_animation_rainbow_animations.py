# SPDX-FileCopyrightText: 2021 Kattni Rembor for Adafruit Industries
# SPDX-FileCopyrightText: Jose David Montoya
# SPDX-License-Identifier: MIT

"""
Rainbow annimations for the LEDSimulation class.
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


rainbow = Rainbow(pixels, speed=0.1, period=2)
rainbow_chase = RainbowChase(pixels, speed=0.1, size=5, spacing=3)
rainbow_comet = RainbowComet(pixels, speed=0.1, tail_length=7, bounce=True)
rainbow_sparkle = RainbowSparkle(pixels, speed=0.1, num_sparkles=15)


animations = AnimationSequence(
    rainbow,
    rainbow_chase,
    rainbow_comet,
    rainbow_sparkle,
    advance_interval=5,
    auto_clear=True,
)

while True:
    rainbow_sparkle.animate()
