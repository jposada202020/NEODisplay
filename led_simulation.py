# SPDX-FileCopyrightText: Copyright (c) 2025 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

"""

`neodisplay`
================================================================================

CircuitPython library to simulate a LED display with NeoPixels using displayio.

* Author: Jose D. Montoya

Adapted for the LEDSimulation class from Adafruit_CircuitPython_LED_Animation library.

"""


import displayio
from vectorio import Circle


def color_to_tuple(value: int):
    """Converts a color from a 24-bit integer to a tuple.

    :param value: RGB desired value - can be a RGB tuple or a 24-bit integer.

    """
    if isinstance(value, tuple):
        return value
    if isinstance(value, int):
        if value >> 24:
            raise ValueError("Only bits 0->23 valid for integer input")
        r = value >> 16
        g = (value >> 8) & 0xFF
        b = value & 0xFF
        return [r, g, b]

    raise ValueError("Color must be a tuple or 24-bit integer value.")


def tuple_to_color(rgb_tuple):
    """Converts an RGB tuple to a 24-bit integer.

    :param rgb_tuple: A tuple containing the RGB values.
    :return: A 24-bit integer representing the color.
    """
    if not isinstance(rgb_tuple, tuple) or len(rgb_tuple) != 3:
        raise ValueError("Input must be an RGB tuple with three elements.")

    r, g, b = rgb_tuple
    if not (0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255):
        raise ValueError(
            "Each element in the RGB tuple must be between 0 and 255."
        )

    return (r << 16) | (g << 8) | b


class LED_Circle:
    def __init__(
        self,
        x,
        y,
        radius=10,
        color=0xFFFFFF,
        pixel_shader=None,
        color_index=1,
        register_width: int = 2,
    ) -> None:

        self.r, self.g, self.b = color_to_tuple(color)

        self.buffer = bytearray(register_width)
        self.array = bytearray(register_width)
        self.led_circle = Circle(
            pixel_shader=pixel_shader,
            radius=radius,
            x=x,
            y=y,
            color_index=color_index,
        )


class LEDSimulation:
    """LEDSimulation class for CircuitPython"""

    def __init__(
        self,
        display,
        led_count=8,
        led_spacing=8,
        led_radius=4,
        led_color=0xFFFFFF,
        auto_write=False,
    ):
        self.display = display
        self.display.auto_refresh = auto_write
        self.led_count = led_count
        self.led_spacing = led_spacing
        self.led_radius = led_radius
        self.led_color = led_color
        self.leds_list = []
        self.group = displayio.Group()
        self.palette = displayio.Palette(256)

        self.palette[0] = 0x000000
        self.palette[1] = led_color
        self._palette_counter = 2
        self._palette_helper = [0x000000, led_color]

        self._start = 10

        self._plotbitmap = displayio.Bitmap(display.width, display.height, 3)
        self.create_leds()
        self.display.root_group = self.group

        LED_Circle(10, 10, 10, 0xFF0000, self.palette)

    def create_leds(self):
        for i in range(self.led_count):

            led = LED_Circle(
                x=self._start + (i * self.led_spacing),
                y=self.display.height // 2,
                radius=self.led_radius,
                color=self.led_color,
                pixel_shader=self.palette,
                color_index=1,
            )

            self.leds_list.append(led)
            self.group.append(led.led_circle)

    def fill(self, color):
        self.palette[1] = color

    def show(self):
        self.display.refresh()

    def __repr__(self):
        return [(led.r, led.g, led.b) for led in self.leds_list]

    def __iter__(self):
        return iter(self.leds_list)

    def __getitem__(self, index):
        return (
            self.leds_list[index].r,
            self.leds_list[index].g,
            self.leds_list[index].b,
        )

    def __len__(self):
        return len(self.leds_list)

    def __setitem__(self, index, color):

        if isinstance(color, int):
            self.palette[self._palette_counter] = color
            converted_color = color_to_tuple(color)
            self.leds_list[index].r = converted_color[0]
            self.leds_list[index].g = converted_color[1]
            self.leds_list[index].b = converted_color[2]
            self.leds_list[index].led_circle.color_index = self._palette_counter
            self._palette_counter += 1
        else:
            for index, element in enumerate(color):
                if element == 0:
                    self.leds_list[index].r = 0
                    self.leds_list[index].g = 0
                    self.leds_list[index].b = 0
                    self.leds_list[index].led_circle.color_index = 0
                else:
                    converted_color = tuple_to_color(element)
                    if converted_color not in self.palette:
                        self.palette[self._palette_counter] = converted_color
                        self._palette_helper.append(converted_color)
                        color_position_in_palette = self._palette_counter
                        self._palette_counter += 1
                    else:
                        color_position_in_palette = self._palette_helper.index(
                            converted_color
                        )
                    self.leds_list[index].r = element[0]
                    self.leds_list[index].g = element[1]
                    self.leds_list[index].b = element[2]
                    self.leds_list[index].led_circle.color_index = (
                        color_position_in_palette
                    )
