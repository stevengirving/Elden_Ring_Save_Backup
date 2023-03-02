from shutil import copyfile
from datetime import datetime
from os import path, makedirs, chdir

# Reference: C:\Users\sgirv\AppData\Roaming\EldenRing\76561197990706360\

elden_save = path.join(path.expanduser("~"), "AppData", "Roaming" , \
                        "EldenRing","76561197990706360")
# Change to save folder
chdir(elden_save)

now = datetime.now().isoformat(timespec="minutes")

# Ask user input for save name
backup_name = input("Please enter a name for your backup: ") + "_" + now

# Confirm input
print(f"Saving backup as \"{backup_name}\".", \
        "Press enter to continue or CTRl-C to stop")
input()

backup_folder = path.join(elden_save, "backup", backup_name)

# Check and make folder Backup/
if path.exists(path.join(elden_save, "backup")) is False:
    makedirs(backup)

makedirs(backup_folder)

chdir(backup_folder)

solo_save = path.join(elden_save, "ER0000.sl2")
coop_save = path.join(elden_save, "ER0000.co2")

# Copy files to backup; reference: ER0000.co2 or ER0000.sl2
copyfile(solo_save, "ER0000.sl2")
copyfile(coop_save, "ER0000.co2")

print("Saved!") 
