from __future__ import print_function

import time
import sys

import Adafruit_DHT as DHT

from nanpy import SerialManager
from nanpy import ArduinoApi

# Arduino Nano v3 is first usb serial device and at /dev/ttyUSB0
# 
# DHT11 sensor connected to Raspberry Pi GPIO pin 4 (physical 7)
# 
# Moisture power input connected to Arduino Nano digital pin 5,
# while analog data output connected to Arduino analog pin 1

connection = SerialManager(device='/dev/ttyUSB0')
arduino = ArduinoApi(connection=connection)

arduino.pinMode(15, arduino.INPUT)
arduino.pinMode(5, arduino.OUTPUT)

# Turn on moisture sensor power
arduino.digitalWrite(5, arduino.HIGH)

print('Waiting 5 seconds')
for i in range(5):
    time.sleep(1)
    sys.stdout.write('.')
    sys.stdout.flush()
print('')

humidity, temperature = DHT.read_retry(11, 4)
moisture = arduino.analogRead(15)

# Turn off moisture sensor power
arduino.digitalWrite(5, arduino.LOW)

connection.close()

print('Temperature %dC' % temperature)
print('Humidity %d%%' % humidity)
print('Moisture %d' % moisture)
