from pymycobot.mycobot import MyCobot
import time

mc = MyCobot('/dev/ttyAMA0',1000000)
mc.power_on()

mc.send_angles([0,0,0,0,0,0],100)
time.sleep(1)
mc.send_angles([-73.82, -28.56, -0.43, 20.12, 24.78, 7.82],100)
time.sleep(0.6)
mc.send_angles([0.0, -73.38, 0.08, 47.54, 17.57, 7.2],100)
time.sleep(0.6)
mc.send_angles([41.3, -87.18, 0.17, 22.41, -2.02, 7.2],100)
time.sleep(0.6)
mc.send_angles([73.03, -49.3, 6.59, 57.56, -64.51, 7.2],100)
time.sleep(0.6)
mc.send_angles([-6.32, -75.93, 6.32, 42.09, -23.2, 50.71],100)
time.sleep(0.4)
mc.send_angles([-75.76, -105.2, 6.67, 76.99, -2.98, 50.7],100)
time.sleep(0.4)
mc.send_angles([0,0,0,0,0,0],100)
time.sleep(1)

