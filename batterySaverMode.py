#!/usr/bin/python3
import os
print('checking for battery conservation option in system files')
batteryConservationFile = "/sys/bus/platform/drivers/ideapad_acpi/VPC2004*/conservation_mode"
try:
    mode = os.popen(f'cat {batteryConservationFile}').read()
    if "1" in mode:
        print('\33[31m turning battery conservation mode OFF')
        os.system(f"echo '0' | sudo tee -a {batteryConservationFile} > /dev/null")
        print(" ⛔")
    else:
        print('\33[32m turning battery conservation mode ON')
        os.system(f"echo '1' | sudo tee -a {batteryConservationFile} > /dev/null")
        print(" ✅")
except:
    print('battery conservation mode not found')
