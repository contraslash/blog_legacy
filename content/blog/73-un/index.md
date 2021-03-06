---
title: "Montar NTFS en Mac"
date: "2016-01-29T06:42:23+00:00"
description: ""
tags: "mac,OSX"
---
# Montar NTFS en Mac

Taked from [here](http://apple.stackexchange.com/a/170011)

Quickly mount a NTFS disk read/write on all recent OS X (including Yosemite, El Capitan):

Open Application -> Utilities -> Terminal
Type mount and look for the line with your disk. It will show something like: /dev/disk3s1 on /Volumes/MyDisk (ntfs, local, noowners, nobrowse)
Type the following in the Terminal, replacing /dev/diskXsX with your disk as shown in the mount command:

sudo mkdir /Volumes/Mount  
*Make sure that the device is not already mounted, if yes, please unmount it first. Otherwise it will result in error: mount_ntfs: /dev/diskNsN on /Volumes/Mount: Resource busy

sudo umount /Volumes/<device_name>
sudo mount -o rw,auto,nobrowse -t ntfs /dev/diskXsX /Volumes/Mount/
open /Volumes/Mount/
To make this change permanent run the following (correct for El Capitan):

Run the following command, changing /dev/diskXsX to your disk:

export DEVICE=/dev/diskXsX   
echo UUID=`diskutil info $DEVICE | grep UUID | awk '{print $3}'` none ntfs rw,auto,nobrowse 
echo LABEL=NTFS none ntfs rw,auto,nobrowse
Run sudo vifs and paste in the output from the previous 2 lines. To do this press down to go to the bottom of the file, A to start adding text, paste in the 2 lines then press escape and :wq to write the file. (vifs is the only safe way to edit the fstab in OS X).

Run the following to mount the disk

sudo umount /Volumes/$DEVICE 
sudo diskutil mountDisk $DEVICE
sudo open `mount | grep $DEVICE | awk '{print $3}'`
Note: The device will no longer automatically open a window when you attach it. To access it open a Finder window and select the Go -> Go to Folder to /Volumes


