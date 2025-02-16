# SPDX-FileCopyrightText: 2021 Kattni Rembor for Adafruit Industries
# SPDX-FileCopyrightText: 2025 Jose D. Montoya
# SPDX-License-Identifier: MIT

"""
Example of the Chase animation using the LEDSimulation Library.
"""
import board
from animation.chase import Chase
from color import CYAN
from led_simulation import LEDSimulation


# Defintions
pixel_num = 30
display = board.DISPLAY

# Create a LEDSimulation object
pixels = LEDSimulation(
    display, led_count=30, led_spacing=9, led_radius=4, led_color=0x000000
)

chase = Chase(pixels, speed=0.5, size=4, spacing=6, color=CYAN)

while True:
    chase.animate()
