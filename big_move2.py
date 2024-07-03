from pymycobot.mycobot import MyCobot
import time

mc = MyCobot('/dev/ttyAMA0',1000000)

mc.power_on()

mc.send_angles([0,0,0,0,0,0],100)
time.sleep(0.8)
mc.send_angles([-39.55, -15.64, 12.12, -9.22, 1.93, -9.22],100)
time.sleep(0.4)
mc.send_angles([10.81, -57.21, 7.11, 27.77, 36.38, 0.61],100)
time.sleep(0.4)
mc.send_angles([45.79, -92.46, 7.55, 35.77, 37.35, -38.58],100)
time.sleep(0.4)
mc.send_angles([84.46, -43.5, 7.47, 51.41, -68.64, -34.89],100)
time.sleep(0.4)
mc.send_angles([13.18, -72.94, 7.2, 45.52, -22.76, -34.89],100)
time.sleep(0.4)
mc.send_angles([-33.48, -99.49, 7.55, 50.62, -10.28, -28.56],100)
time.sleep(0.4)
mc.send_angles([-33.48, -3.6, 7.47, -6.06, -2.19, -28.56],100)
time.sleep(0.7)
mc.send_angles([0,0,0,0,0,0],100)
time.sleep(0.8)
