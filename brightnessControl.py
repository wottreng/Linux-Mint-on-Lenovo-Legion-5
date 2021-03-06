#!/usr/bin/env python3
'''
[*] install into your system Path and bind to brightness keys to control screen brightness
[-->] see github writeup for more info: https://github.com/wottreng/Linux-Mint-on-Lenovo-Legion-5

[\/] version 2.2: fix explicit setting for all screens with just `-s XX`
'''
import os
import sys


class brightnessControl:
    def __init__(self):
        self.verbose = False
        self.version = 2.2
        self.specificDevice = False
        self.device = ""
        self.connectedDevices = []
        self.currentBrightness = ""
        self.requested_brightness = 50
        self.systemDeviceSetup = {}

    def setBrightness(self, device: str, brightness: int):
        minimum_brightness = 20
        maximum_brightness = 100
        if brightness > maximum_brightness:
            brightness = maximum_brightness
        elif brightness < minimum_brightness:
            brightness = minimum_brightness
        brightnessPercent = (brightness / 100)
        if self.verbose: print(f"\033[92m[+]\033[0m set brightness for {device} to {brightnessPercent}")
        os.system(f"xrandr --output {device} --brightness {brightnessPercent}")  # set the brightness

    def getDisplayDevices(self):
        if self.verbose: print("\033[95m[#]\033[0m finding all connected display devices")
        allDevices = os.popen("xrandr --prop | grep 'connected'").readlines()
        for line in allDevices:
            if "disconnected" not in line:
                device_name = line.split(" ")[0]
                self.connectedDevices.append(device_name)
        if self.verbose: print(f"\033[95m[*]\033[0m Your Display Devices = {self.connectedDevices}")

    def getAllDisplayDevicesBrightness(self):
        brightnessOutput = os.popen("xrandr --prop --verbose | grep -A10 'connected' | grep 'Brightness'").readlines()
        x = 0
        for device in self.connectedDevices:
            print(f"\033[95m-->\033[93m {device} {brightnessOutput[x].strip()}\033[0m")  # display device settings
            self.systemDeviceSetup[device] = brightnessOutput[x].strip().split(" ")[1]
            x += 1

    def check_and_update(self):
        current_version_text = os.popen("curl https://raw.githubusercontent.com/wottreng/Linux-Mint-on-Lenovo-Legion-5/main/brightnessControl.py").read()
        location_of_version = current_version_text.find("self.version = ")
        latest_version = current_version_text[location_of_version + 15: location_of_version + 18]
        print(f"\033[95m your version: {self.version}, latest version: {latest_version} \033[0m")
        if float(latest_version) > self.version:
            print("\033[94m[*]\033[0m updating script to latest version")
            script_path = os.popen("which brightnessControl.py").read().strip()
            print(f"\033[95m-->\033[0m script path: {script_path}")
            file_stats = os.stat(script_path)
            # print(f"file stats: {file_stats}")
            with open("/tmp/temp_file", "w") as temp_file:
                temp_file.write(current_version_text)
            if file_stats.st_uid == 0:
                print("\033[91m[!]\033[0m Root owns the script, Please input admin password to update script")
                os.system(f"sudo cat /tmp/temp_file > {script_path}")
            else:
                print("\033[92m[*]\033[95m Updating script file")
                os.system(f"cat /tmp/temp_file > {script_path}")
            print("\033[95m[*]\033[0m update completed! ")


if __name__ == '__main__':
    BC = brightnessControl()
    # args: h: help, c: change by X amount, d: device, s: set brightness, v: verbose
    if "-h" in sys.argv:
        print("\033[95m----------------------------------------------------\033[93m")
        print("Brightness Control\033[95m")
        print("\033[94margs:\033[95m")
        print("-c: change brightness by percent, ex. '-c 5' or '-c -5'")
        print("-d: set display device, ex. your auxiliary screen: '-d HDMI-0'")
        print("-s: set brightness value directly, ex. '-s 60'")
        print("-u: check version on Github and update")
        print("-v: verbose, you like to read lots of text")
        print("----------------------------------------------------\033[0m")
        quit()
    if "-v" in sys.argv:
        BC.verbose = True
    BC.getDisplayDevices()
    print("----- current values ------")
    BC.getAllDisplayDevicesBrightness()
    print("---------------------------")
    if "-d" in sys.argv:
        index = sys.argv.index("-d")
        BC.device = sys.argv[index + 1]
        BC.specificDevice = True
        if BC.device not in BC.connectedDevices:
            print('incorrect device name')
            quit()
        if BC.verbose: print(f"device chosen: {BC.device}")
    if "-c" in sys.argv:
        index = sys.argv.index("-c")
        amount = int(sys.argv[index + 1])  # use 5 or -5 to change brightness by 5%
        if not BC.specificDevice:  # apply to all
            for device, brightnessPercent in BC.systemDeviceSetup.items():
                brightness = int((float(brightnessPercent) * 100) + amount)
                BC.setBrightness(device=device, brightness=brightness)
        else:
            brightnessPercent = BC.systemDeviceSetup[BC.device]
            brightness = int((float(brightnessPercent) * 100) + amount)
            BC.setBrightness(device=BC.device, brightness=brightness)
        print("----- new values ------")
        BC.getAllDisplayDevicesBrightness()
        print("---------------------------")
        quit()

    if "-s" in sys.argv:
        if BC.verbose: print("\033[95m[->]\033[0m setting display brightness directly")
        index = sys.argv.index("-s")
        try:
            BC.requested_brightness = int(sys.argv[index + 1])  # value between 0 and 100
        except Exception as e:
            print(f'not an accepted value: {e}')
            quit()
        if BC.verbose: print(f"requested brightness: {BC.requested_brightness}")
        if BC.device != "":
            BC.setBrightness(device=BC.device, brightness=BC.requested_brightness)
        else:
            print("\033[95m[*]\033[0m no device chosen, applying setting to all")
            for device in BC.connectedDevices:
                if BC.verbose: print(f"\033[93m[-]\033[90m device: {device}, set brightness to: {BC.requested_brightness} %")
                BC.setBrightness(device=device, brightness=BC.requested_brightness)
        quit()
    if "-u" in sys.argv:
        BC.check_and_update()
    # ----
    if BC.verbose: print("\033[95mset display brightness based on system values\033[0m")
    for device, brightnessPercent in BC.systemDeviceSetup.items():
        brightness = int(float(brightnessPercent) * 100)
        BC.setBrightness(device=device, brightness=brightness)
    if BC.verbose: BC.getAllDisplayDevicesBrightness()

    quit()
