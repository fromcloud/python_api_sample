#!/bin/bash

# creating vm, partition and format 2nd disk.
echo -e "o\nn\np\n1\n\n\nw" | fdisk /dev/xvdb
fdisk -t ext4 /dev/xvdb1
mount /dev/xvdb1 /mnt
echo "/dev/xvdb1		/mnt			ext4	defaults	0 0" >> /etc/fstab
