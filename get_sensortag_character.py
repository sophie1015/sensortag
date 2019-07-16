#!/usr/bin/python

from bluepy import btle
import sys
 
MAC = sys.argv[1]

print("Connecting...")
dev = btle.Peripheral(MAC)
 
lightSensor = btle.UUID("f000aa70-0451-4000-b000-000000000000")
 
print("Characteristics...")
lightService = dev.getServiceByUUID(lightSensor)
for ch in lightService.getCharacteristics():
    print(str(ch))

