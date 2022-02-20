# SPDX-FileCopyrightText: 2021 Kevin Matocha
#
# SPDX-License-Identifier: MIT
#############################
"""
Use the random throttle effect for the Dial.
"""

import time
import board
import displayio
import terminalio
from displayio_dial import Dial

# Fonts used for the Dial tick labels
tick_font = terminalio.FONT

display = board.DISPLAY  # create the display on the PyPortal or Clue (for example)
# otherwise change this to setup the display
# for display chip driver and pinout you have (e.g. ILI9341)


# Define the minimum and maximum values for the dial
minimum_value = 0
maximum_value = 100

# Create a Dial widget
my_dial = Dial(
    x=20,  # set x-position of the dial inside of my_group
    y=20,  # set y-position of the dial inside of my_group
    width=180,  # requested width of the dial
    height=180,  # requested height of the dial
    padding=25,  # add 25 pixels around the dial to make room for labels
    start_angle=-120,  # left angle position at -120 degrees
    sweep_angle=240,  # total sweep angle of 240 degrees
    min_value=minimum_value,  # set the minimum value shown on the dial
    max_value=maximum_value,  # set the maximum value shown on the dial
    tick_label_font=tick_font,  # the font used for the tick labels
    tick_label_scale=2.0,  # the scale factor for the tick label font
)


my_group = displayio.Group()
my_group.append(my_dial)

display.show(my_group)  # add high level Group to the display

# Set the dial to the
my_dial.value = 50

my_dial.throttle_effect = 5  # Fluctuate at most "5" in either direction
my_dial._throttle_move_rate = 0.1  # Fluctuate at "0.1" per throttle_update()

while True:

    my_dial.throttle_update()
    # display.refresh()
