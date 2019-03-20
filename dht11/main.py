# Tested on M5Stack Gray
# DHT11 sensor module. see https://www.switch-science.com/catalog/818/
from m5stack import lcd
from machine import DHT, Pin
import time

dht = DHT(Pin(22))

lcd.clear()
lcd.font(lcd.FONT_Default, fixedwidth=True)

while True:
    result, temperature, humidity = dht.read()
    if result:
        lcd.println('Temperature: {} degrees'.format(temperature), 0, 0, color=lcd.GREEN)
        lcd.println('Humidity:    {} %'.format(humidity), color=lcd.GREEN)
        time.sleep(60)
