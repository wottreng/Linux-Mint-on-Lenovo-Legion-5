timeStamp: `13 September 2021`

# Linux-Mint-on-Lenovo-Legion-5 💻
### How to install Linux Mint on Legion 5 to have proper hardware drivers and screen brightness control 
Linux Mint is forked from Debian and similar to Ubuntu so this may work for Ubuntu OS as well. \
I did try to install Ubuntu 21.xx OS and it created a custom NVIDIA driver that didnt quite work properly so be warned.

I hope this will help someone else that might be going down this same path. \
It took me a while to figure it out so hopefully I can same you some time.

Laptop: Lenovo Legion 5 15 Gaming Laptop, 15.6" FHD (1920 x 1080) Display, AMD Ryzen 7 5800H Processor, 16GB DDR4 RAM, 512GB NVMe SSD, NVIDIA GeForce RTX 3050Ti  
Amazon link: https://www.amazon.com/dp/B08YKG5K7F

Linux Mint OS: https://linuxmint.com/

these are the steps I took to get Linux Mint 20.2 Cinnamon v. 4.4.8 on a Lenovo Legion 5 gaming laptop \ 
(text in perenthesis is what worked for me at the time of writing this)
## OS installation:
* install linux mint OS onto thumb drive 
* insert thumbdrive into laptop
* boot laptop while pressing `F12` - this will let you choose boot device
* select thumbdrive to boot OS installer
* install Linux Mint

## STEPS to get Hardware operating properly [this will get graphics card to cooperate with OS for proper operation]: 

1: install latest linux kernel (kernel: 5.11.0-34-generic) 
  * `sudo mintupdate` : Mint Update Manager GUI
  * using 'Update Manager' gui : credit: https://www.makeuseof.com/upgrade-kernel-linux-mint/ 
  * Update Manager -> View -> Linux Kernels -> (5.11) -> install 
  
2: isntall latest nvidia graphics drivers (470.63.01) 
  * using "driver manager" gui update graphics drivers to latest nvidia driver version 
  * `sudo mintdrivers` : Mint Driver Update GUI
  * then install latest NVIDIA proprietary driver

## STEPS to get screen brightness to work correctly and brightness keys to actually change brightness:

1: generate xorg.conf file: `sudo nvidia-xconfig` 
  * this command comes with latest nvidia drivers installed in prior steps to graphics card working 
  * this will generate /etc/X11/xorg.conf \
  ref: https://askubuntu.com/questions/217758/how-to-make-an-xorg-conf-file
  
2: add `"EnableBrightnessControl=1"` to xorg.conf file inside device section 
  * you need to add the whole line: `Option         "RegistryDwords" "EnableBrightnessControl=1"`
  * `sudo gedit /etc/X11/xorg.conf` or `sudo nano /etc/X11/xorg.conf`
  * add line in device section: \
   <b> example: <b>
  ```
    Section "Device" 
      Identifier     "Device0" 
      Driver         "nvidia" 
      VendorName     "NVIDIA Corporation" 
      Option         "RegistryDwords" "EnableBrightnessControl=1" 
    EndSection 
 ```  
 3: reboot system and X11 will pick up the new configuration and your brightness function keys will now work 
 
 ## Realtek wifi 6 working with proper drivers:
 see this github for proper drivers: https://github.com/lwfinger/rtw89
 * git clone https://github.com/lwfinger/rtw89.git -b v5
 * cd rtw89
 * make
 * sudo make install
 * sudo modprobe rtw89pci 
 
 ## Battery Saver mode
 * run `batterySaverMode.py` to put laptop into battery saver mode when plugged in
 * limits charging above 60%
 
 ## Other helpful tips
 * ` F2 ` : open BIOS during boot
 * ` Ctrl + Alt + F1 ` : change to basic command line interface
 * ` Ctrl + Alt + F7 ` : change back to GUI 'desktop' interface
 * hold `Shift` during boot to open up grub for advanced options like recovery mode
 
 ### another great reference for legion 5: https://github.com/antony-jr/lenovo-legion5-15arh05-scripts
 
 ## Cheers everyone 🍺 
