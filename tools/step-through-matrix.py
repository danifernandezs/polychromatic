#!/usr/bin/env python3
#
# This script will step through each key in the matrix and
# prompt for a label, to identify what lights up.
#

import razer.client as rclient
print("Successfully imported razer.client")

devman = rclient.DeviceManager()
print("Successfully connected to Device Manager.")

print("\nCurrently connected devices:")
devices = devman.devices
uid = 0
for d in devices:
    print("[{0}] {1} ({2} / {3})".format(uid, d.name, d.type, d.serial))
    uid += 1
print(" ")

use_id = input("Enter device ID: ")
device = devman.devices[int(use_id)]

print("\nThis script will step through each avaliable co-ordinate. Note down what the key is then press ENTER to continue.")
print("\n----------------------------------------\n")
print(device.name + " (type: " + device.type + ")")
if not device.has("lighting_led_matrix"):
    print("Sorry, this device does not support the matrix.")
    exit()

total_rows = device.fx.advanced.rows
total_cols = device.fx.advanced.cols
print("Rows:    " + str(total_rows))
print("Columns: " + str(total_cols))

print("\nX, Y    Label")
for row in range(0, total_rows):
    for col in range(0, total_cols):
        device.fx.advanced.matrix[row, col] = [0, 255, 0]
        device.fx.advanced.draw()
        input("{0}, {1} = ".format(str(row), str(col)))
        device.fx.advanced.matrix[row, col] = [0, 0, 0]

input("\nReached the end. Be sure to save this, then press ENTER to quit.")
