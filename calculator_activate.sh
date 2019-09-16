#!/bin/bash
# This script switches focus to gnome-calculator if it is running.
# If it is not running, it will run gnome-calculator.

if [ "$(wmctrl -l | grep 'Calculator$')" != "" ]; then
    wmctrl -a "Calculator"
else
    gnome-calculator &
fi