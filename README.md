timeStamp: `29 November 2021`

# Linux-Mint-on-Lenovo-Legion-5 💻
### How to install Linux Mint on Legion 5 to have proper hardware drivers and screen brightness control 
Linux Mint is forked from Debian and similar to Ubuntu so this may work for Ubuntu OS as well. \
I did try to install Ubuntu 21.xx OS and it created a custom NVIDIA driver that didnt quite work properly so be warned.

I hope this will help someone else that might be going down this same path. \
It took me a while to figure it out so hopefully I can same you some time.

Laptop: Lenovo Legion 5 15 Gaming Laptop, 15.6" FHD (1920 x 1080) Display, AMD Ryzen 7 5800H Processor, 16GB DDR4 RAM, 512GB NVMe SSD, NVIDIA GeForce RTX 3050Ti  
Amazon link: https://www.amazon.com/dp/B08YKG5K7F or my affliate link if you would like to support me: https://amzn.to/3s9NQcC

Linux Mint OS: https://linuxmint.com/

these are the steps I took to get Linux Mint 20.2 Cinnamon v. 4.4.8 on a Lenovo Legion 5 gaming laptop 
- (text in perenthesis is what worked for me at the time of writing this)

## OS installation:
* READ THE DOCS: https://linuxmint-installation-guide.readthedocs.io/en/latest/
* install linux mint OS onto thumb drive 
* insert thumbdrive into laptop
* boot laptop while pressing `F12` - this will let you choose boot device
* select thumbdrive to boot OS installer
* install Linux Mint

## STEPS to get Hardware operating properly [this will get graphics card to cooperate with OS for proper operation]: 

1: install latest linux kernel (kernel: 5.11.0-34-generic) 
  * cli cmd: `sudo mintupdate` ➡ Mint Update Manager GUI
  * write up for 'Update Manager' gui : credit: https://www.makeuseof.com/upgrade-kernel-linux-mint/ 
  * GUI steps: Update Manager ➡ View ➡ Linux Kernels ➡ (5.11) ➡ install 
  
2: install latest nvidia graphics drivers (470.63.01) \
using "driver manager" gui update graphics drivers to latest nvidia driver version 
  * cli cmd: `sudo mintdrivers` ➡ Mint Driver Update GUI
  * then install latest NVIDIA proprietary driver

## STEPS to get screen brightness to work correctly and brightness keys to actually change screen brightness:

1: generate xorg.conf file ➡ cli cmd: `sudo nvidia-xconfig` 
  * this command comes with latest nvidia drivers installed in prior steps to get graphics card working 
  * this will generate `/etc/X11/xorg.conf` file\
  * the `xorg.conf` file is used by Xorg to configure your display settings\
  ref: https://www.x.org/releases/current/doc/man/man5/xorg.conf.5.xhtml \
  ref: https://askubuntu.com/questions/217758/how-to-make-an-xorg-conf-file
  
2: add `"EnableBrightnessControl=1"` to xorg.conf file inside device section 
  * NOTE: you need to add the whole line: `Option         "RegistryDwords" "EnableBrightnessControl=1"`
  * cli cmd: `sed '/NVIDIA Corporation/a \    Option\t   "RegistryDwords" "EnableBrightnessControl=1"' /etc/X11/xorg.conf | sudo tee /etc/X11/xorg.conf` 

   <b> example: <b>
  ```
    Section "Device" 
      Identifier     "Device0" 
      Driver         "nvidia" 
      VendorName     "NVIDIA Corporation" 
      Option         "RegistryDwords" "EnableBrightnessControl=1" 
    EndSection 
 ```
 
 3: download this repository ➡ cli cmd: `git clone https://github.com/wottreng/Linux-Mint-on-Lenovo-Legion-5.git`
 
 4: change directory ➡ cli cmd: `cd Linux-Mint-on-Lenovo-Legion-5/`
 
 5: make setupBrightnessControlKeys.sh excutable ➡ cli cmd: `chmod 777 setupBrightnessControlKeys.sh`
 
 6: run setup script ➡ cli cmd: `./setupBrightnessControlKeys.sh`
 
 * your brightness keys will now work properly!
 * Read `setupBrightnessControlKeys.sh` for comments on how this works and how to remove key bindings if needed
 
 ## Realtek wifi 6 working with proper drivers:
 Repository for driver: https://github.com/lwfinger/rtw89 \
 CLI commands:
 * git clone https://github.com/lwfinger/rtw89.git
 * cd rtw89
 * make
 * sudo make install
 * sudo modprobe -v rtw89pci 
 
 These commands are compiled in the script: `installRTW89wifiDriver` \
 ⚠ NOTE: this entire process needs to be repeated on every kernel update ⚠
 
 ## Battery Saver mode
 * run `batterySaverMode.py` to put laptop into battery saver mode when plugged in
 * limits charging above 60% capacity
 
 1: add script to $PATH (ex. your `/bin` folder) ➡ `/bin/batterySaverMode.py` \
  * cli cmd: `sudo mv ./batterySaverMode.py /bin/batterySaverMode.py`
 
 2: make it excutable ➡ cli cmd: `sudo chmod 777 /bin/batterySaverMode.py`
 
 3: call it from a command line ➡ cli cmd: `batterySaverMode.py`
 
 ## Other helpful tips
 * ` F2 ` : open BIOS during boot
 * ` Ctrl + Alt + F1 ` : change to basic command line interface
 * ` Ctrl + Alt + F7 ` : change back to GUI 'desktop' interface
 * hold `Shift` during boot to open up grub for advanced options like recovery mode
 * open cli: `CTRL + ALT + T`
 
 ### another great reference for legion 5: https://github.com/antony-jr/lenovo-legion5-15arh05-scripts
 
 ### Please contribute 📥 or message me if there is a better way! Lets help the Linux Community! 👌
 
 ### Next Steps & Noted Issues
 * sleep function does not work correctly - screen goes blank after wake
 * bluetooth becomes unresponsive randomly - could be bluez bluetooth software issue'
 * hybrid graphics, currently using discrete graphics only 
 
 ## Cheers everyone 🍺 
