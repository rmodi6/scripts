#!/bin/bash
# Script to mount windows bitlocker partition on linux
set -e
mkdir -p /media/bitlocker
mkdir -p /media/mount
sudo dislocker -V /dev/nvme1n1p3 -- /media/bitlocker -o nonempty
sudo mount -o loop /media/bitlocker/dislocker-file /media/mount

mkdir -p /media/ntfs
sudo mount -t ntfs /dev/nvme0n1p2 /media/ntfs