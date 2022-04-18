timeStamp: `12 March 2022`

** updated for Linux Mint 20.3 Cinnamon** \
** updated for power consumption issue fix **

# Linux-Mint-on-Lenovo-Legion-5 💻
### How to install Linux Mint on Legion 5 to have proper hardware drivers and screen brightness control 
Linux Mint is forked from Debian and similar to Ubuntu so this may work for Ubuntu OS as well. \
I did try to install Ubuntu 21.xx OS and it created a custom NVIDIA driver that didnt quite work properly so be warned.

I hope this will help someone else that might be going down this same path. \
It took me a while to figure it out so hopefully I can same you some time.

Laptop: Lenovo Legion 5 15 Gaming Laptop, 15.6" FHD (1920 x 1080) Display, AMD Ryzen 7 5800H Processor, 16GB DDR4 RAM, 512GB NVMe SSD, NVIDIA GeForce RTX 3050Ti  
Amazon link: https://amzn.to/3s9NQcC

Linux Mint OS: https://linuxmint.com/

these are the steps I took to get Linux Mint 20.3 Cinnamon on a Lenovo Legion 5 gaming laptop 
- (text in perenthesis is what worked for me at the time of writing this)

## OS installation:
* READ THE DOCS: https://linuxmint-installation-guide.readthedocs.io/en/latest/
* install linux mint OS onto thumb drive 
* insert thumbdrive into laptop
* boot laptop while pressing `F12` - this will let you choose boot device
* select thumbdrive to boot OS installer
* select install Linux Mint on live media Desktop

## STEPS to get Hardware operating properly: 
[NOTE: hybrid graphics started working in Mint 20.3. For older versions, see older commits for discrete graphics only setup] \
1: select hybrid graphics [NOTE: you can select Discrete Graphics if you want]
 * boot laptop while pressing `F2` on keyboard
 * once in UEFI firmware settings, select hybrid graphics
 * select `Exit` and save settings

2: install latest linux kernel (kernel: 5.13.0-21-generic) 
  * cli cmd: `sudo mintupdate` ➡ Mint Update Manager GUI
  * write up for 'Update Manager' gui : credit: https://www.makeuseof.com/upgrade-kernel-linux-mint/ 
  * GUI steps: Update Manager ➡ View ➡ Linux Kernels ➡ (5.13) ➡ install 
  * reboot laptop ➡ cli cmd: `reboot`
  
3: install latest nvidia graphics drivers (510.47.03) \
using "driver manager" gui update graphics drivers to latest nvidia driver version 
  * cli cmd: `sudo mintdrivers` ➡ Mint Driver Update GUI
  * then install latest NVIDIA proprietary driver
  * reboot laptop ➡ cli cmd: `reboot`
  * [--NOTE: if you selected DISCRETE graphics, stop here--]
  * after reboot and login, click on `NVIDIA On-Demand` icon in lower right applet panel
  * click `NVIDIA Settings`
  * click `PRIME Profiles`
  * click `NVIDIA On-Demand`
  * after authentication and changes made, select `Quit`
  * reboot laptop ➡ cli cmd: `reboot`

4: update all packages to latest versions
* GUI: select `Update Manager` in App Menu
* cli cmd: `sudo apt update && sudo apt full-upgrade -y`
* clean out garbage and fix links: `sudo apt autoremove && sudo apt autoclean`

## STEPS to get screen brightness to work correctly and brightness keys to actually change screen brightness:
 ** update for Mint 20.3 Cinnamon, script updated to make fix device name convention bug ** \
NOTE: brightness keys still not working so use this repository to control brightness in software

TLDR cli magic (copy and paste into your cmd line): 
```markdown
wget https://github.com/wottreng/Linux-Mint-on-Lenovo-Legion-5/archive/refs/heads/main.zip && unzip main.zip && cd Linux-Mint-on-Lenovo-Legion-5-main && chmod 777 setupBrightnessControlKeys.sh && ./setupBrightnessControlKeys.sh
```

git setup:
 
 1: download this repository ➡ cli cmd: `git clone https://github.com/wottreng/Linux-Mint-on-Lenovo-Legion-5.git`
 
 2: change directory ➡ cli cmd: `cd Linux-Mint-on-Lenovo-Legion-5/`
 
 3: make setupBrightnessControlKeys.sh excutable ➡ cli cmd: `chmod 777 setupBrightnessControlKeys.sh`
 
 4: run setup script ➡ cli cmd: `./setupBrightnessControlKeys.sh` 

 5: test your brightness keys, they should work properly now! If not see trouble shooting below
 
[-- NOTES -- ]
 * Read `setupBrightnessControlKeys.sh` for comments on how this works and how to remove key bindings if needed
 * run `brightnessControl.py -h` for help output and supported arguments
 * for TROUBLE SHOOTING or changes see `Keyboard` in App Menu ➡ `Shortcuts` ➡ `Custom Shortcuts` 
 * Common issue with script is it finding the wrong device name. Run `brightnessControl.py -v` to see what device names its finding and you may need to set default in your key bindings like so: `brightnessControl.py -d DEV-NAME -c 5` 

 ## Realtek wifi 6 working with proper drivers:
 ⚠ NOTE: wifi driver is now included in Mint 20.3. If you still need drivers then look at older commits for manual install process ⚠
 
 ## Battery Saver mode
 * `batterySaverMode.py` puts laptop into battery saver mode when plugged in
 * limits charging above 60% capacity

TLDR cli magic (copy and paste into your cmd line): 
```markdown
wget https://github.com/wottreng/Linux-Mint-on-Lenovo-Legion-5/archive/refs/heads/main.zip && unzip main.zip && cd Linux-Mint-on-Lenovo-Legion-5-main && chmod 777 batterySaverMode.py && sudo mv ./batterySaverMode.py /bin/
```
 
 1: make it excutable ➡ cli cmd: `chmod 777 ./batterySaverMode.py`

 2: add script to $PATH (ie. your `/bin` folder) ➡ `/bin/batterySaverMode.py` 
  * cli cmd: `sudo mv ./batterySaverMode.py /bin/batterySaverMode.py`
  
 3: call it from a command line ➡ cli cmd: `batterySaverMode.py`
 
 ## Power Consumption Configuration
 (credit goes to [O491dogan](https://github.com/O491dogan)) \
 Higher than normal power consumption has been reported after proper drivers and updates. \
 The issue seems to be the dGPU not being turned off when not in use.
 
 * check power consumption with `powertop`
   - `sudo apt install powertop`
   - optimize system consumption with `sudo powertop --auto-tune`
   - launch with `sudo powertop` with power cable unplugged
     - with nothing running, power consumption should be about 10w.
     - if dGPU is running, power consumption is about 25w. 
 * Make sure dGPU is set to on-demand
   - set dGPU to adaptive in BIOS
   - set dGPU to On-Demand in NVIDIA settings
     - `nvidia-settings` then select PRIME Profiles, then select NVIDIA On-Demand
 * Confirm dGPU is set to On-Demand
   - cmd: `cat /sys/bus/pci/devices/0000:01:00.0/power/control` 
     - should output `auto` for dGPU on-demand
     - `on` your dGPU is always on
 * Battery Life
   - with dGPU always on, about 2 hours
   - with dGPU on-demand, about 4 to 5 hours
   
 NOTES: \
 more info, see [discussion](https://github.com/wottreng/Linux-Mint-on-Lenovo-Legion-5/discussions/3)
 
 
 ## Other helpful tips
 * ` F2 ` : open BIOS during boot
 * ` Ctrl + Alt + F1 ` or  ` Ctrl + Alt + F2 `: change to basic command line interface
 * ` Ctrl + Alt + F7 ` : change back to GUI 'desktop' interface
 * hold `Shift` during boot to open up grub for advanced options like recovery mode
 * open cli: `CTRL + ALT + T`
 
 ### another great reference for legion 5: https://github.com/antony-jr/lenovo-legion5-15arh05-scripts
 
 ### Please contribute 📥 or message me if there is a better way! Lets help the Linux Community! 👌
 
 ### Noted Issues
 * check Issues tab 
 
 ## Cheers everyone 🍺 

<a href=" https://www.buymeacoffee.com/wottreng" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>
