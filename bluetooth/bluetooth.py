##
# Uses blueutil and BluetoothConnector to automatically turn on 
# bluetooth, connect to a bluetooth device and turn off bluetooth after
# disconnection.
##

import time
import subprocess

def bluetooth_status():
    return int(subprocess.Popen("/usr/local/bin/blueutil --power", shell=True, stdout=subprocess.PIPE).stdout.read().decode("utf-8"))

def is_bluetooth_connected():
    return 'Connected: Yes' in subprocess.Popen("system_profiler SPBluetoothDataType", shell=True, stdout=subprocess.PIPE).stdout.read().decode("utf-8")

def bluetooth(power):
    subprocess.call(['/usr/local/bin/blueutil', '--power', str(power)])
    subprocess.call(['say', 'Bluetooth turned on' if power else 'Bluetooth turned off'])

def connect_to_device(mac_addr):
    subprocess.call(['/usr/local/bin/BluetoothConnector', '--connect', mac_addr, '--notify'])

sleep_time = 90
wait_time = 60
mac_addr = 'INSERT-MAC-ADDRESS-HERE'

toggle = 1 - bluetooth_status()
bluetooth(toggle)

if bluetooth_status():
    connect_to_device(mac_addr)
    while True:
        while bluetooth_status() and is_bluetooth_connected():
            print('Bluetooth on and connected. Sleep.')
            time.sleep(sleep_time)
        print('Bluetooth off or disconnected. Waiting to connect...')
        time.sleep(wait_time)
        if not is_bluetooth_connected():
            print('Bluetooth still disconnected. Exit.')
            break
    bluetooth(0)
else:
    print('Bluetooth is off. Exit.')