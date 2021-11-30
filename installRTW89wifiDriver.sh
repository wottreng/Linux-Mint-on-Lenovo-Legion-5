#!/bin/bash
# READ the DOCS: https://github.com/lwfinger/rtw89
echo "cloning rtw89 repository..."
git clone https://github.com/lwfinger/rtw89.git -b v5
cd rtw89
echo "build driver..."
make
echo "install driver..."
sudo make install
echo "activate driver..."
sudo modprobe rtw89pci
echo "wifi should work now, Cheers"
