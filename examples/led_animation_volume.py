# SPDX-FileCopyrightText: 2023 Tim Cocks
#
# SPDX-License-Identifier: MIT

"""Volume Animation Example for NeoDisplay
This example works, however this willl need asyncio to show the volume animation."""

import board
from audiomp3 import MP3Decoder
from led_simulation import LEDSimulation
from animation import volume

try:
    from audioio import AudioOut
except ImportError:
    try:
        from audiopwmio import PWMAudioOut as AudioOut
    except ImportError:
        pass  # not always supported by every board!

# Defintions
pixel_num = 30
display = board.DISPLAY

# Fill in your own MP3 file or use the one from the learn guide:
# https://learn.adafruit.com/circuitpython-essentials/circuitpython-mp3-audio#installing-project-code-3067700
mp3file = "happy.mp3"
with open(mp3file, "rb") as mp3:

    decoder = MP3Decoder(mp3)
    audio = AudioOut(board.SPEAKER)

    pixels = LEDSimulation(
        display, led_count=30, led_spacing=9, led_radius=4, led_color=0x000000
    )
    volume_anim = volume.Volume(pixels, 0.3, (0, 255, 0), decoder, 400)

    while True:
        audio.play(decoder)

        while audio.playing:
            volume_anim.animate()
