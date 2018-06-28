#!/bin/sh

folder="/private/var/Jamf/OS/Current"


file=$(ls $folder)
echo $file

$folder/"$file"/Contents/Resources/startosinstall --rebootdelay 1 --nointeraction ‑‑eraseinstall ‑‑agreetolicense && killall "Self Service"
