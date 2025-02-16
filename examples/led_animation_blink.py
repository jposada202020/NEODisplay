# SPDX-FileCopyrightText: 2021 Kattni Rembor for Adafruit Industries
# SPDX-FileCopyrightText: 2025 Jose D. Montoya
# SPDX-License-Identifier: MIT

"""
This example blinks the LEDs purple at a 0.5 second interval in a simulated LED display.
Adapted for the LEDSimulation class from Adafruit_CircuitPython_LED_Animation library.

"""
import board
from led_simulation import LEDSimulation
from animation.blink import Blink
from color import PURPLE
import board


# Defintions
pixel_num = 30
display = board.DISPLAY


# Create a LEDSimulation object
pixels = LEDSimulation(
    display, led_count=50, led_spacing=9, led_radius=4, led_color=0xFF0000
)

# Main functiones to test the LEDSimulation object
print(f"Pixels: {pixels}")
print(f"Length of pixels: {len(pixels)}")
print(f"Pixel 0: {pixels[0]}")
print(f"Pixel 1: {pixels[1]}")
print(dir(pixels))

# Create a Blink object
blink = Blink(pixels, speed=0.5, color=PURPLE)

# Run the animation
while True:
    blink.animate()
