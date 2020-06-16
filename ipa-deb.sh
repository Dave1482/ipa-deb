#!/bin/bash

echo "
██╗██████╗░░█████╗░░░░░░░██████╗░███████╗██████╗░
██║██╔══██╗██╔══██╗░░░░░░██╔══██╗██╔════╝██╔══██╗
██║██████╔╝███████║█████╗██║░░██║█████╗░░██████╦╝
██║██╔═══╝░██╔══██║╚════╝██║░░██║██╔══╝░░██╔══██╗
██║██║░░░░░██║░░██║░░░░░░██████╔╝███████╗██████╦╝
╚═╝╚═╝░░░░░╚═╝░░╚═╝░░░░░░╚═════╝░╚══════╝╚═════╝░
"

echo "Original script in python by CaspD3V"
echo "Bash script version by Dave1482"
echo ""
read -p 'IPA File Name (do not input the full path or the .ipa extension) : ' file
if [ ! -f "$file.ipa" ]; then
echo "$file.ipa does not exist, exiting..."
exit 1
fi
source="$file.ipa"
dest="$file.zip"

echo "
Turning IPA Into ZIP..."
mv $source $dest
echo "Done Renaming."

mkdir -p ./Extracted
echo "Extracting Archive..."
unzip -qq $dest -d ./Extracted
echo "Done Extracting."
cd Extracted

rm -f * 2>/dev/null
source1="Payload"
dest1="Applications"
echo "Making Applications Folder"
mv $source1 $dest1
echo "Making DEBIAN Folder"
mkdir ./DEBIAN
cd DEBIAN

echo "
Making control File... Please input package information
"
read -p "Package ID (ex: com.yourname.yourpackagename) : " bid
read -p "Name (ex: YourPackageName) : " name
read -p "Version (ex: 1.0.0) : " ver
read -p "Description (ex: An awesome App!): " desc
read -p "Maintainer (ex: YourName <your@email.com>): " maintain
read -p "Author (ex: YourName <your@email.com>): " auth
echo "Package: $bid
Name: $name
Version: $ver
Architecture: iphoneos-arm
Description: $desc
Maintainer: $maintain
Author: $auth
Section: Applications
" > control
echo "
Done With control File..."

cd ..
echo "Packaging Deb..."
dpkg-deb -b . ..
cd ..
echo "Cleaning Up..."
mv $dest $source
rm -rf ./Extracted

echo "Done!"
