# tested on M5Stack Gray
# based on http://blog.akanumahiroaki.com/entry/2018/10/27/235000
from m5stack import lcd
from machine import I2C
from mpu9250 import MPU9250
import time

i2c = I2C(sda=21, scl=22)
sensor = MPU9250(i2c)

lcd.clear()

x, y = 0, 0

while True:
    ax, ay, az = sensor.acceleration
    ax = ax * -1  # original is left negative

    # clear previous ball
    lcd.circle(x, y, 5, lcd.BLACK, lcd.BLACK)

    # g-bowl
    lcd.circle(160, 120, 110, lcd.WHITE)
    lcd.circle(160, 120, 55, lcd.WHITE)
    lcd.line(50, 120, 270, 120, lcd.WHITE)
    lcd.line(160, 10, 160, 230, lcd.WHITE)

    # plot ball
    x = int(ax * (55 / 10)) + 160
    y = int(ay * (55 / 10)) + 120
    lcd.circle(x, y, 5, lcd.RED, lcd.RED)

    time.sleep_ms(20)
