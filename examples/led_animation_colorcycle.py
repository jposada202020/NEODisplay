# SPDX-FileCopyrightText: 2021 Kattni Rembor for Adafruit Industries
# SPDX-FileCopyrightText: 2025 Jose David Montoya
# SPDX-License-Identifier: MIT

"""
ColorCycle example for LEDSimulation
"""
import board
from led_simulation import LEDSimulation
from animation.colorcycle import ColorCycle
from color import (
    TEAL,
    MAGENTA,
    ORANGE,
)

# Defintions
pixel_num = 30
display = board.DISPLAY

# Create a LEDSimulation object
pixels = LEDSimulation(
    display, led_count=30, led_spacing=9, led_radius=4, led_color=0x000000
)

colorcycle = ColorCycle(pixels, speed=0.4, colors=[MAGENTA, ORANGE, TEAL])


while True:
    colorcycle.animate()
