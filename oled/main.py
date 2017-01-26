from machine import I2C, ADC
from ssd1306 import SSD1306 as ssd
i2c = I2C(0, I2C.MASTER, baudrate=400000)
d = ssd(height=64, external_vcc=0)
d.poweron()
d.init_display()
d.invert_display(0)
d.draw_text(10, 0, 'WiPy', size=2, space=2)
d.draw_text(0, 20, 'MicroPython', size=1, space=2)
d.display()
count=0
adc = ADC(0)
adc_c = adc.channel(pin='P16')

while 1:
    d.draw_text(0, 40, 'VBatt %.1f V' % (adc_c.value() *3.3/4095), size=2)
    d.display()
