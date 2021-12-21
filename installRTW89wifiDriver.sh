#!/bin/bash
# READ the DOCS: https://github.com/lwfinger/rtw89

set -e # exit if an error occurs

echo -e "\033[1;32m [*] cloning rtw89 repository... \033[0m"
git clone https://github.com/lwfinger/rtw89.git

echo -e "\033[0;33m [*] changing directory to rtw89 repository \033[0m"
cd rtw89/

echo -e "\033[1;33m [*] build driver... \033[0m"
make

echo -e "\033[1;33m [*] install driver... \033[0m"
sudo make install

echo -e "\033[1;31m [*] removing old kernel module driver... \033[0m"
sudo modprobe -v -r rtw89pci

echo -e "\033[0;33m [*] activating new kernel module driver... \033[0m"
sudo modprobe -v rtw89pci

echo -e "\033[0;32m [*] wifi should work now, Cheers 🍻 \033[0m"
