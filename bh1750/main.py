import time
from machine import I2C
import bh1750fvi
i2c = I2C(0, I2C.MASTER, baudrate=100000)
light_sensor = bh1750fvi.BH1750FVI(i2c, addr=0x23)
while(True):
    data = light_sensor.read()
    print(data)
    time.sleep(1)
