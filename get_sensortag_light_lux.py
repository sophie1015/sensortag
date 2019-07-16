#!/usr/bin/python

from bluepy import btle
import binascii
import time
import sys
import struct
import math
 
MAC = sys.argv[1]

print("Connecting...")
dev = btle.Peripheral(MAC)
 
#print("Services...")
for svc in dev.services:
    #print(str(svc))
    pass

lightSensor = btle.UUID("f000aa70-0451-4000-b000-000000000000")
 
lightService = dev.getServiceByUUID(lightSensor)
for ch in lightService.getCharacteristics():
    #print(str(ch))
    pass

uuidConfig = btle.UUID("f000aa72-0451-4000-b000-000000000000")
lightSensorConfig = lightService.getCharacteristics(uuidConfig)[0]

# Enable the sensor
lightSensorConfig.write(bytes("\x01"))
 
time.sleep(1.0) # Allow sensor to stabilise
 
uuidValue  = btle.UUID("f000aa71-0451-4000-b000-000000000000")
lightSensorValue = lightService.getCharacteristics(uuidValue)[0]

while True:
    # Read the sensor
    val = lightSensorValue.read()
    print "val: ", binascii.b2a_hex(val)

    # Convert raw
    raw = struct.unpack('<h', val)[0]
    m = raw & 0xFFF;
    e = (raw & 0xF000) >> 12;
    print "lux: ", str(0.01 * (m << e))

    time.sleep(1)

