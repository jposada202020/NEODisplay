# SPDX-FileCopyrightText: 2025 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

"""
Pacman example for LEDSimulation
"""
import board
from led_simulation import LEDSimulation
from animation.pacman import Pacman
from color import WHITE

# Defintions
pixel_num = 30
display = board.DISPLAY

# Create a LEDSimulation object
pixels = LEDSimulation(
    display, led_count=30, led_spacing=9, led_radius=4, led_color=0x000000
)

# Create the Pacman animation object
pacman = Pacman(pixels, speed=0.4, color=WHITE)

# Main loop
while True:
    pacman.animate()
