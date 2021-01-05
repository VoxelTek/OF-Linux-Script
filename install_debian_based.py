import os
import time

from subprocess import Popen

a = 0 #Placeholder variable so that 'input' below will work as I want it to.

os.system("sudo apt install subversion") #Installs Subversion, if it isn't already installed.
os.system("cd ~/.steam/steam/steamapps/sourcemods") #Changes the current working directory to the sourcemods/ folder.

os.system("svn checkout https://svn.openfortress.fun/svn/open_fortress/ ~/.steam/steam/steamapps/sourcemods/open_fortress") #Clones, or "checkouts" the Open Fortress files from the SVN repository, into "open_fortress" in the sourcemods/ directory.

#os.system("steam steam://rungameid/243750")
steamProcc = Popen('steam steam://rungameid/243750')
time.sleep(5)
os.system("pkill hl2_linux")

a = input("Press enter when Source SDK 2013 Multiplayer has completed installing.")

os.system("pkill steam") #Kills Steam
#os.system("steam") #Restarts Steam

steamProcc = Popen('steam')

print("The install should now be completed. Open Fortress should now appear in your Steam library. If you have any issues, join this discord server:")
print("https://discord.gg/Jk3NUb7")
print("And ping @VoxelTek#7809 in #linux-troubleshooting")

print("")

print("If Open Fortress claims that you are playing insecure, add:")
print("-secure -steam")
print("to Open Fortress's launch options.")

print("")

time.sleep(10)

print("Auto-launching Open Fortress in...")
time.sleep(2)
print("5")
time.sleep(1)
print("4")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)

os.system("steam steam://rungameid/243750 -game ~/.local/share/Steam/steamapps/sourcemods/open_fortress -secure -steam")
