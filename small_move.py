from pymycobot.mycobot import MyCobot
import time

mc = MyCobot('/dev/ttyAMA0',1000000)
mc.power_on()

mc.send_angles([0,0,0,0,0,0],100)
time.sleep(1)
mc.send_angles([-23.81, -51.94, -7.82, 58.53, -13.97, 33.57],100)
time.sleep(0.8)
mc.send_angles([44.12, -64.59, -7.38, 66.79, -27.59, 33.57],100)
time.sleep(0.8)
mc.send_angles([-25.92, -54.75, -7.2, 58.0, 3.07, 33.57],100)
time.sleep(0.8)
mc.send_angles([38.23, -54.49, -6.94, 76.99, 3.07, 33.48],100)
time.sleep(0.8)
mc.send_angles([0,0,0,0,0,0],100)
time.sleep(1)

