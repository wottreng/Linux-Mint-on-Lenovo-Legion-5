# Linux-Mint-on-Lenovo-Legion-5
how to install Linux Mint on Legion 5 to have proper hardware drivers and screen brightness control

I hope this will help someone else that might be going down this same path.
It took me a while to figure it out so hopefully I can same you some time.

Laptop: Lenovo Legion 5 15 Gaming Laptop, 15.6" FHD (1920 x 1080) Display, AMD Ryzen 7 5800H Processor, 16GB DDR4 RAM, 512GB NVMe SSD, NVIDIA GeForce RTX 3050Ti  
Amazon link: https://www.amazon.com/dp/B08YKG5K7F

Linux Mint OS: https://linuxmint.com/

timeStamp: 13 September 2021

these are the steps I took to get Linux Mint 20.2 Cinnamon v. 4.4.8 on a Lenovo Legion 5 gaming laptop
(text in perenthesis is what worked for me at the time of writing this)
STEPS to get Hardware operating properly [this will get graphics card to cooperate with software for proper operation]: 
1: install latest linux kernel (kernel: 5.11.0-34-generic)
  a: using 'Update Manager' gui : credit: https://www.makeuseof.com/upgrade-kernel-linux-mint/
2: isntall latest nvidia graphics drivers (470.63.01)
  a: using "additional drivers" gui update graphics drivers to latest nvidia driver version

STEPS to get screen brightness to work correctly and brightness keys to actually change brightness:
1: generate xorg.conf file: { sudo nvidia-xconfig }
  ref: https://askubuntu.com/questions/217758/how-to-make-an-xorg-conf-file
  a: this command comes with latest nvidia drivers installed in prior steps to graphics card working  
  b: this will generate /etc/X11/xorg.conf
2: add `Option         "RegistryDwords" "EnableBrightnessControl=1"` to xorg.conf file inside device section
  a: { sudo gedit /etc/X11/xorg.conf }
  b: add `Option         "RegistryDwords" "EnableBrightnessControl=1"` in device section
    example: 
    Section "Device"
      Identifier     "Device0"
      Driver         "nvidia"
      VendorName     "NVIDIA Corporation"
      Option         "RegistryDwords" "EnableBrightnessControl=1"
    EndSection
 3: reboot system and X11 will pick up the new configuration and your brightness function keys will now work
 

