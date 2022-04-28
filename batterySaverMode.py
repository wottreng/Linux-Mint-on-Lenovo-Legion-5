#!/usr/bin/python3
import os

battery_conservation_file_path = "/sys/bus/platform/drivers/ideapad_acpi/VPC2004:00/conservation_mode"

if os.path.isfile(battery_conservation_file_path):
    with open(battery_conservation_file_path, "r") as file:
        current_mode = file.read()
    if "1" in current_mode:
        print('--> mode is currently ON\n\33[91m [!] set battery conservation mode OFF\33[0m')
        os.system(f"echo '0' | sudo tee -a {battery_conservation_file_path} > /dev/null")
        print("done ✅")
    else:
        print('--> mode is currently OFF\n\33[92m 🔋set battery conservation mode ON 🔋\33[0m')
        os.system(f"echo '1' | sudo tee -a {battery_conservation_file_path} > /dev/null")
        print("done ✅")
else:
    print(f"battery conservation file does not exist at path: \n {battery_conservation_file_path}")
