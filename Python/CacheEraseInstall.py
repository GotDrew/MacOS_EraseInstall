#!/usr/bin/python
# Import libraries for basic command line functions
import os, sys

# Enable this in live... or if you dont like your computer
live = False

# Vars
if live:
	folder="/private/var/Jamf/OS/Current/"
	if not os.path.exists(folder):
		print "Current doesn't exist so we're out of here..."
		if live: sys.exit()
else: # just use test folders on the desktop
    folder="/Users/arh/Desktop/Test/OS/Current/"

# Find the MacOS install app
if live: file = os.listdir(folder)[0]
else: file = "MacOS Installer.app"
file = file.replace(" ", "\ ") # fix the string for running commands

# Run the update!
print "Running the file located here: "+folder+file
if live: os.system(folder+file+"/Contents/Resources/startosinstall --rebootdelay 1 --nointeraction ‑‑eraseinstall ‑‑agreetolicense && killall 'Self Service'")
else: print "We're testing Mate, should've worked though..."
