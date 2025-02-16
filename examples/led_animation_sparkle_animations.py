# SPDX-FileCopyrightText: 2021 Kattni Rembor for Adafruit Industries
# SPDX-License-Identifier: MIT

"""
This example uses AnimationsSequence to display multiple animations in sequence, at a five second
interval.

For NeoPixel FeatherWing. Update pixel_pin and pixel_num to match your wiring if using
a different form of NeoPixels.
"""
import board
from led_simulation import LEDSimulation

from animation.sparkle import Sparkle
from animation.sparklepulse import SparklePulse
from sequence import AnimationSequence
from color import AMBER, JADE

# Defintions
pixel_num = 30
display = board.DISPLAY

# Create a LEDSimulation object
pixels = LEDSimulation(
    display, led_count=30, led_spacing=9, led_radius=4, led_color=0x000000
)


sparkle = Sparkle(pixels, speed=0.05, color=AMBER, num_sparkles=10)
sparkle_pulse = SparklePulse(pixels, speed=0.05, period=3, color=JADE)

animations = AnimationSequence(
    sparkle,
    sparkle_pulse,
    advance_interval=5,
    auto_clear=True,
)

while True:
    animations.animate()
