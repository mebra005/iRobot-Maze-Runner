#!/usr/bin/env python3


from breezycreate2 import Robot
import time

import serial
import time
import sys

time.sleep( 1 )
ser = serial.Serial('/dev/ttyACM0', 9600)
ser.flushInput()

#check distance from ultrasonic sensor on Arduino
def checkDistance():
    value = ser.readline()
    distance = float(value)
    return distance


# Create a Create2. This will automatically try to connect to your robot over serial
bot = Robot()

# Play a note to let us know you're alive!
bot.playNote('A4', 100)
time.sleep(2)


while True:
    ser.flushInput()
    bot.setForwardSpeed(50)
    if 2 <= checkDistance() <= 15:
        bot.setForwardSpeed(0)
        bot.setTurnSpeed(-30)
        time.sleep(6)
        bot.setTurnSpeed(0)
	time.sleep(2)
        ser.flushInput()
        if 2 <= checkDistance() <= 17:
            bot.setTurnSpeed(30)
            time.sleep(12)
            bot.setTurnSpeed(0)
            ser.flushInput()
            if 2 <= checkDistance() <= 17:
                bot.setForwardSpeed(0)
                bot.playNote('A4', 100)
                bot.setTurnSpeed(200)
                bot.playNote('A3', 100)
                time.sleep(1)
                bot.playNote('A2', 100)
                time.sleep(1)
                bot.playNote('B4', 100)
                time.sleep(1)
                bot.setTurnSpeed(0)
                # Close the connection
                bot.close()
                break
