Title: Getting the trackpoint working on the Thinkpad X240
Date: 2015-09-24 14:00
Category: coding

TrackPoint scrolling doesn't work out of box, but you can easily fix it by yourself. All you need is:

 1) Add `psmouse.proto=bare` option to you kernel during boot

Open `/etc/default/grub`
Modify the GRUB_CMDLINE_LINUX option (e.g. `GRUB_CMDLINE_LINUX="psmouse.proto=bare` ....)
As a root run `grub2-mkconfig -o /boot/grub2/grub.cfg`

 2) Create /usr/share/X11/xorg.conf.d/11-trackpoint-wheel-emulation.conf

:::yaml
	Section "InputClass"
	    Identifier      "Trackpoint Wheel Emulation"
	    MatchProduct    "PS/2 Generic Mouse"
	    MatchDevicePath "/dev/input/event*"
	    Option          "EmulateWheel" "true"
	    Option          "EmulateWheelButton" "2"
	    Option          "EmulateWheelTimeout" "200"
	    Option          "YAxisMapping" "4 5"
	    Option          "XAxisMapping" "6 7"
	EndSection


3) Reboot
