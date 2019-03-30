#!/bin/bash
##
## ctv 1200 720
## edit file /usr/share/lightdm/lightdm.conf.d/50-unity-greeter.conf
## add string: "display-setup-script=path-to-this-script"
##
xrandr --newmode "1200x720_60.00"   69.50  1200 1256 1376 1552  720 723 730 748 -hsync +vsync
xrandr --addmode LVDS-1 1200x720_60.00
xrandr --output LVDS-1 --mode 1200x720_60.00

