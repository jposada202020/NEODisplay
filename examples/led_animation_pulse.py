# SPDX-FileCopyrightText: 2025 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

"""
Pulse example for LEDSimulation
"""
import board
from led_simulation import LEDSimulation
from animation.pulse import Pulse
from color import AMBER

# Defintions
pixel_num = 30
display = board.DISPLAY

# Create a LEDSimulation object
pixels = LEDSimulation(
    display, led_count=30, led_spacing=9, led_radius=4, led_color=0x000000
)

pulse = Pulse(pixels, speed=0.1, color=AMBER, period=3)

while True:
    pulse.animate()
