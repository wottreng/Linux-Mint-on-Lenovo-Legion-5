#!/usr/bin/python3
import os
import sys


def setBrightness(device: str, brightnessPercent: float):
    os.system(f"xrandr --output {device} --brightness {brightnessPercent}")


def getDisplayDevices():
    allDevices = os.popen("xrandr --prop | grep 'connected'").readlines()
    connected_devices = []
    for line in allDevices:
        if "disconnected" not in line:
            device_name = line.split(" ")[0]
            connected_devices.append(device_name)
    print(f"display devices = {connected_devices}")
    return connected_devices


def getAllDisplayDevicesBrightness(devices=None):
    brightnessOutput = os.popen("xrandr --prop --verbose | grep -A10 'connected' | grep 'Brightness'").readlines()
    if type(devices) == list:
        x = 0
        for device in devices:
            print(f"{device} {brightnessOutput[x].strip()}")
            x += 1
    else:
        for line in brightnessOutput:
            print(line)


devices = getDisplayDevices()
getAllDisplayDevicesBrightness(devices)
print("-----------")
# requested_brightness = input("set new display brightness: 0 to 1\n")
if len(sys.argv) == 3:
    device = sys.argv[1]
    requested_brightness = sys.argv[2]
    try:
        requested_brightness = float(requested_brightness)
    except Exception as e:
        print(f'not a float value: {e}')
        quit()
    if device not in devices:
        print('incorrect device name')
        quit()
    requested_brightness = float(requested_brightness)
    if requested_brightness > 1:
        requested_brightness = 1
    elif requested_brightness < 0.1:
        requested_brightness = 0.1
    else:
        print("value accepted and processed")
        setBrightness(device=device, brightnessPercent=requested_brightness)

else:  # no args given
    print("too change brightness, pass args into cli for device and brightness")
    print("ex. \'brightnessControl.py DP-4 0.5\' ")
