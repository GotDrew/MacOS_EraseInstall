#!/usr/bin/python
# Import libraries for basic command line functions
import os, time, sys

# Enable this in live... or if you dont like your computer
live = False

# Vars
if live:
    folder="/private/var/Jamf/OS/"
    subFolder="/private/var/Jamf/OS/Current/"
else:# just use test folders on the desktop
    folder="/Users/arh/Desktop/Test/OS/"
    subFolder="/Users/arh/Desktop/Test/OS/Current/"
    if not os.path.exists(folder):
        print "Making test dirs..."
        os.makedirs("/Users/arh/Desktop/Test/")
        os.makedirs("/Users/arh/Desktop/Test/OS")
        time.sleep(30)

# Firstly check if the folder exists and remove it and anyother installs.
print "House keeping..."
if os.path.exists(subFolder):
    killemAll = os.listdir(subFolder)
    for item in killemAll:
        if live: os.remove(item)
        print item
    if live: os.rmdir(subFolder)
    print "Killed existing Current folder"
else:
    print "Clean Install!"

#Get the MacOS Installer app, we do this before making the subfolder so we can be lazy later
if os.listdir(folder)!=[]:
    file = os.listdir(folder)[0]
    print
    print "Found the file here: "+folder+file
else:
    print "No files in the folder... are you in testing?"
    if live: sys.exit()

# Build the folder we just nuked... cos we can't make up our mind...
print "Making the current folder..."
if live: os.makedirs(subFolder)
if os.path.exists(subFolder):
    print "Built the current folder at: "+subFolder
else: # Something went wrong...
    if os.listdir(folder)==[]:
        print "Something went wrong...No app in the cache folder..."
    else:
        print "Something went wrong...Check the permissions on the private var Jamf folder..."
    if live: sys.exit()

# Move the app to the Current folder
print "Getting it awesome..."
if live: os.rename(folder+file, subFolder+file)
print "We're done here."
