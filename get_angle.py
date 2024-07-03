from pymycobot.mycobot import MyCobot
import time

mc = MyCobot('/dev/ttyAMA0',1000000)

mc.power_on()

angles = mc.get_angles()
print("Current Angles:", angles)

mc.power_off()
