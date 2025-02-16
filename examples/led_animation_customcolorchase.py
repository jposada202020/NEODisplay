# SPDX-FileCopyrightText: 2021 Kattni Rembor for Adafruit Industries,
# SPDX-FileCopyrightText: 2025 Jose David Montoya
# SPDX-License-Identifier: MIT

"""
CustomColorChase example for LEDSimulation
"""
import board
from led_simulation import LEDSimulation
from animation.customcolorchase import CustomColorChase
from sequence import AnimationSequence
from color import colorwheel
from color import PINK, GREEN, RED, BLUE

# Defintions
pixel_num = 30
display = board.DISPLAY

# Create a LEDSimulation object
pixels = LEDSimulation(
    display, led_count=30, led_spacing=9, led_radius=4, led_color=0x000000
)


# colors default to RAINBOW as defined in color.py
custom_color_chase_rainbow = CustomColorChase(
    pixels, speed=0.1, size=2, spacing=3
)
custom_color_chase_rainbow_r = CustomColorChase(
    pixels, speed=0.1, size=3, spacing=3, reverse=True
)

# Example with same colors as RainbowChase
steps = 30
# This was taken from rainbowchase.py
rainbow_colors = [colorwheel(n % 256) for n in range(0, 512, steps)]

# Now use rainbow_colors with CustomColorChase
custom_color_chase_rainbowchase = CustomColorChase(
    pixels, speed=0.1, colors=rainbow_colors, size=2, spacing=3
)

custom_color_chase_bgp = CustomColorChase(
    pixels, speed=0.1, colors=[BLUE, GREEN, PINK], size=3, spacing=2
)

# Can use integer values for color, 0 is black
custom_color_chase_br = CustomColorChase(
    pixels, speed=0.1, colors=[BLUE, 0, RED, 0], size=2, spacing=0
)

animations = AnimationSequence(
    custom_color_chase_rainbow,
    custom_color_chase_rainbow_r,
    custom_color_chase_rainbowchase,
    custom_color_chase_bgp,
    custom_color_chase_br,
    advance_interval=3,
    auto_clear=True,
)

while True:
    animations.animate()
