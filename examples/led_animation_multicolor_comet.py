# SPDX-FileCopyrightText: 2022 Tim Cocks
# SPDX-FileCopyrightText: 2025 Jose David Montoya
# SPDX-License-Identifier: MIT
"""

"""
import board
from led_simulation import LEDSimulation
from animation.multicolor_comet import MulticolorComet

# Defintions
pixel_num = 30
display = board.DISPLAY

# Create a LEDSimulation object
pixels = LEDSimulation(
    display, led_count=30, led_spacing=9, led_radius=4, led_color=0x000000
)


comet_colors = [
    0xFF0000,
    0xFD2000,
    0xF93E00,
    0xF45B00,
    0xEC7500,
    0xE28D00,
    0xD5A200,
    0xC6B500,
    0xB5C600,
    0xA2D500,
    0x8DE200,
    0x75EC00,
    0x5BF400,
    0x3EF900,
    0x20FD00,
    0x00FF00,
]


comet = MulticolorComet(
    pixels,
    colors=comet_colors,
    speed=0.01,
    tail_length=20,
    bounce=True,
    ring=False,
    reverse=False,
)

while True:
    comet.animate()
