#!/usr/bin/python

from bluepy import btle
import sys
 
MAC = sys.argv[1]

print("Connecting...")
dev = btle.Peripheral(MAC)
 
print("Services...")
for svc in dev.services:
    print(str(svc))

