# MacOS_EraseInstall
Some scripts for using the MacOS **startosinstall --eraseinstall** command

## Overview:
1. Add the latest MacOS installer app to the computer then run the setup script.
2. Then there are 3 different scripts
   - one to update the OS 
   - one for eraseinstalls 
   - one for eraseinstall with an MDM enrolment package. 
I've changed it over to Python because _"Learning..."_


## Setup
I'm using Jamf to push out the MacOS installer.app to _"/private/var/Jamf/OS/"_
Then I run **CacheSetup** which clears the old installer, creates a "Current" folder and moves the installer app into it.
If using the **Erase Install Enroll**, the **enrolment package** will need to be added to a folder _"/private/var/Jamf/QA/"_.

## Update
Basic **startosinstall** but I kill **"Self Service"** as a precaution for when I add it to our Self Service.

## Erase Install
Uses the **startosinstall** with the new (10.13.4) **eraseinstall** flag, clears the hdd and installs the cached OS, really good for DEP devices.

## Erase Install Enroll
Grabs the enrolment package from the _"/private/var/Jamf/QA/"_ and converts it for use with the **startosinstall eraseinstall** and **installpackage** flags. 
