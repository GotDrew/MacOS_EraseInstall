#!/bin/sh

folder="/private/var/Jamf/OS/Current"
ls $folder

file=$(ls $folder)
echo "File: " $file

$folder/"$file"/Contents/Resources/startosinstall --rebootdelay 1 --nointeraction && killall "Self Service"
#test
#$folder/"$file"/Contents/Resources/startosinstall --usage
