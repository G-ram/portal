#!/bin/bash
BUS=001
DEVICE=002

sudo rmmod ftdi_sio
sudo rmmod usbserial
lsusb -d 0403:6010
chmod 0666 /dev/bus/usb/$BUS/$DEVICE
