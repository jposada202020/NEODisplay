# SPDX-FileCopyrightText: 2025 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

"""
Solid example for LEDSimulation
"""
import board
from led_simulation import LEDSimulation
from animation.solid import Solid
from color import PINK

# Defintions
pixel_num = 30
display = board.DISPLAY

# Create a LEDSimulation object
pixels = LEDSimulation(
    display, led_count=30, led_spacing=9, led_radius=4, led_color=0x000000
)


solid = Solid(pixels, color=PINK)

while True:
    solid.animate()
