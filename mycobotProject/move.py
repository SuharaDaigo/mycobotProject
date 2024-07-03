from pymycobot.mycobot import MyCobot
import time

mc = MyCobot('/dev/ttyAMA0',1000000)

mc.power_on()

mc.send_angles([0,0,0,0,0,0],100)
time.sleep(1)
mc.send_angles([-159,58,44,0.08,-55,111,-2],100)
time.sleep(1)
mc.send_angles([-46,62,0,-30,140,-2],100)
time.sleep(1)
mc.send_angles([64,56,0.5,-28,90,-3],100)
time.sleep(1)
mc.send_angles([96,40,0.3,-31,51,-4],100)
time.sleep(1)
mc.send_angles([0,0,0,0,0,0],90)
time.sleep(1)

mc.power_off()
