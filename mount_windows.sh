#!/bin/bash
# Script to mount windows bitlocker partition on linux
mkdir -p /media/bitlocker
mkdir -p /media/mount
sudo dislocker -V /dev/nvme0n1p3 -- /media/bitlocker
sudo mount -o loop /media/bitlocker/dislocker-file /media/mount