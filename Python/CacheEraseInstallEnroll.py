#!/usr/bin/python
# Import libraries for basic command line functions
import os

# Enable this in live....
live = False

# Check OS is ready to install...
if not os.path.exists("/private/var/Jamf/OS/Current"):
    print "Current doesn't exist so we're out of here..."
    if live: sys.exit()

# Vars
qaFolder = "/private/var/Jamf/QA/"  # folder caching the QA
qaPkgName = "QA"                    # whatever you want to name it
qaPkg = qaFolder+qaPkgName+".pkg"   # inclues path
osFolder = "/private/var/Jamf/OS/Current/"  # folder caching the OS Installer
osInstallerFlags = " --rebootdelay 1 --nointeraction --eraseinstall --agreetolicense --installpackage "


# Prep the QuickAdd Package for the erase install functions
if os.path.exists(qaFolder):
    qaFile = os.listdir(qaFolder)[0]
    if qaFile.startswith( 'QuickAdd' ):
        print "Building Package"
        if live: os.system("productbuild --package " + qaFolder+qaFile + " " + qaPkg )
else:
    print "QA Folder doesn't exist yet... your jumping the gun here..."

# Initiate the EraseInstall
if live: osFile = os.listdir(osFolder)[0]
print "Prepped for Erase and Install..."
if live: os.system(osFolder+osFile.replace(" ", "\ ")+"/Contents/Resources/startosinstall "+ osInstallerFlags + qaPkg )
else: print "We're testing Mate, should've worked though..."
