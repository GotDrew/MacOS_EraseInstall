#!/bin/sh

folder="/private/var/Jamf/OS/"
subFolder="/private/var/Jamf/OS/Current/"

#Firstly check if the folder exists and remove it and anyother installs.
echo "House keeping..."
if [ -d "$subFolder" ]; then
  rm -rf "$subFolder"
  echo "Killed existing Current"
else
  echo "Clean Install"
fi

file=$(ls "$folder")
echo "$file"
echo "$folder/$file"

#Build the folder we just nuked... cos we can't make up our mind...
echo "Caching Installer"
if [ ! -d "$subFolder" ]; then
  mkdir "$subFolder"
  echo "Built the current folder"
else
  echo "Something went wrong..."
fi

mv "$folder$file" "$subFolder"
