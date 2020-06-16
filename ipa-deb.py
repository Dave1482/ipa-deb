import sys
import zipfile
import os
import shutil
import time

print('''

██╗██████╗░░█████╗░░░░░░░██████╗░███████╗██████╗░
██║██╔══██╗██╔══██╗░░░░░░██╔══██╗██╔════╝██╔══██╗
██║██████╔╝███████║█████╗██║░░██║█████╗░░██████╦╝
██║██╔═══╝░██╔══██║╚════╝██║░░██║██╔══╝░░██╔══██╗
██║██║░░░░░██║░░██║░░░░░░██████╔╝███████╗██████╦╝
╚═╝╚═╝░░░░░╚═╝░░╚═╝░░░░░░╚═════╝░╚══════╝╚═════╝░
	''')
print('By CaspD3V ;)')
file = input("IPA File Name: ")
source = ''+file+'.ipa'
dest = ''+file+'.zip'
os.rename(source, dest) 
print("Turning IPA Into ZIP...") 
print("Done Renaming.") 
with zipfile.ZipFile(''+file+'.zip', 'r') as zip_ref:
    zip_ref.extractall('Extracted')

    print("Extracting Archive..") 
    time.sleep(20)
    print("Done Extracting.")
os.chdir('Extracted')
source1 = 'Payload'
dest1 = 'Applications'
print("Making Applications Folder")
os.rename(source1, dest1) 
path = "DEBIAN"
try:
	os.mkdir(path)
except OSError:
	print ("Creation of the directory %s failed" % path)
else:
	print ("Successfully created the directory %s " % path)
print("Making DEBIAN Folder")
os.chdir('DEBIAN')
print("Making control File")
bid = input("Package ID (ex: com.yourname.yourpackagename) : ")
name = input("Name (ex: YourPackageName) : ")
ver = input("Version (ex: 1.0.0) : ")
desc = input("Description (ex: An awesome App!): ")
maintain = input("Maintainer (ex: YourName <your@email.com>): ")
auth = input("Author (ex: YourName <your@email.com>): ")
f = open('control',"w+")
for i in range(1):
	f.write('Package: '+bid+'\nName: '+name+'\nVersion: '+ver+'\nArchitecture: iphoneos-arm\nDescription: '+desc+'\nMaintainer: '+maintain+'\nAuthor: '+auth+'\nSection: Applications\n')
f.close()
print("Done With Control File...") 
os.chdir('../')
print("Packaging Deb..")
os.system('dpkg-deb -b . ..')
os.chdir('../')
print("Cleaning Up..")
source2 = ''+file+'.zip'
dest2 = ''+file+'.ipa'
os.rename(source2, dest2)
removedir = "Extracted"
shutil.rmtree(removedir)
