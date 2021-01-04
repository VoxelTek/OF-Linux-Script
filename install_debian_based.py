import os
import time

a = 0 #Placeholder variable so that 'input' below will work as I want it to.

os.system("sudo apt install subversion") #Installs Subversion, if it isn't already installed.
os.system("cd ~/.local/share/Steam/steamapps/sourcemods") #Changes the current working directory to the sourcemods/ folder.

os.system("svn checkout https://svn.openfortress.fun/svn/open_fortress/ open_fortress") #Clones, or "checkouts" the Open Fortress files from the SVN repository, into "open_fortress" in the sourcemods/ directory.

os.system("steam steam://rungameid/243750")
time.sleep(5)
os.system("pkill hl2_linux")

a = input("Press enter when Source SDK 2013 Multiplayer has completed installing.")

os.system("pkill steam") #Kills Steam
os.system("steam") #Restarts Steam

print("The install should now be completed. Open Fortress should now appear in your Steam library. If you have any issues, join this discord server:")
print("https://discord.gg/Jk3NUb7")
print("And ping @VoxelTek#7809 in #linux-troubleshooting")

print("If Open Fortress claims that you are playing unsecure, add:")
print("-secure -steam")
print("to Open Fortress's launch options.")


time.sleep("10")

print("Auto-launching Open Fortress in...")
time.sleep("2")

time.sleep("1")

time.sleep("1")

time.sleep("1")

time.sleep("1")

time.sleep("1")

os.system("steam steam://rungameid/243750 -game ~/.local/share/Steam/steamapps/sourcemods/open_fortress -secure -steam")
