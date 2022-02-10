#!/bin/bash

# How this works:
# first, make this script excutable: `chmod 777 setupBrightnessControlKeys.sh`
# second, make sure `keyBindgings.conf` is in the same folder as this script
# third, run this script to bind brightnessControl.py to brightness keys

echo "setting up key bindings for brightness control"
echo "moving script into your /bin \$PATH...."
sudo mv ./brightnessControl.py /bin/brightnessControl.py
echo "making brightnessControl.py excutable..."
sudo chmod 777 /bin/brightnessControl.py
echo "saving your current key bindings just in case..."
dconf dump /org/cinnamon/desktop/keybindings/ > OldKeyBindings.dconf
echo "loading custom key bindings into dconf..."
dconf load /org/cinnamon/desktop/keybindings/ < keyBindings.dconf
echo "[*] try your brightness keys now, they should work [*]"

# CLI: check key bindings: dconf dump /org/cinnamon/desktop/keybindings/

# GUI: check config: Menu -> Keyboard -> Shortcuts -> Custom Shortcuts
# your custom key bindings will be displayed in the GUI i.e. `cinnamon-settings`.

# HOW TO REMOVE KEY BINDINGS: Menu -> Keyboard -> Shortcuts -> Custom Shortcuts
# click on the custom keyboard shortcut and then click Remove custom shortcut button

#Cheers, Mark W.
