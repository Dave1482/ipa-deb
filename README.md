# IPA-DEB

This is a tool to turn any ipa into an installable deb file for jailbroken iOS devices.

## Setup

1. Make a folder and put ipa-deb.py or ipa-deb.sh & your iPA in the folder.
2. Open Terminal and cd into thet folder.
3. Give the script permissions shown below
```bash
chmod +x ipa-deb*
```

## Requirements

1. Device with dpkg 
2. Python3 or bash
3. Terminal

## How To Use

Python3
```bash
python3 ipa-deb.py
```
Bash
```bash
./ipa-deb.sh
```

1. Type the ipa file name.
Example:
```bash
ipaname
```
2. Leave it running until it prompts your to enter the control file fields.

## Control File
Bundle ID:
Example:
```bash
com.example.app
```
Name:
Example:
```bash
App Name
```
Version:
Example:
```bash
1.0.0
```
Description:
Example:
```bash
This is my super cool app!
```
Maintainer:
Example:
```bash
Username
```
Author:
Example:
```bash
Username
```

## Final Thoughts

This tool makes it easy to create packages and it takes no time at all :)


## Developer's Websites

[Casp's Website](https://casp.dev)
[Dave1482's Website](http://dave1482.com)
