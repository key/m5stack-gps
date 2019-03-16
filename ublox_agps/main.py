# Autor: Jesús Sánchez Sänchez (gokuhs)
# Based on veproza proyect: https://gist.github.com/veproza/55ec6eaa612781ac29e7
import gc
import struct
from binascii import hexlify

import urequests
import utime
from machine import UART
from checksum import calc_checksum

token = 'TOKEN HERE'

gps_s = UART(2, tx=17, rx=16, baudrate=9600, timeout=200, buffer_size=256, lineend='\r\n')

print('Connecting to u-blox')
r = urequests.get(
    'http://online-live1.services.u-blox.com/GetOnlineData.ashx?token=' + token + ';gnss=gps;datatype=eph,alm,aux,pos;filteronpos;format=aid',
    stream=True,
)
print(r)
print('Downloading A-GPS data')

print('Waiting to GPS be free')
drainer = True
while drainer:
    drainer = gps_s.any()
    if drainer > 0:
        gps_s.read(drainer)

print('Writing AGPS data')
gps_s.write(r.content)
print('Done')

# RXM Configuration
print('Writing configuration')
header = struct.pack('BBBBH', 0xb5, 0x62, 0x06, 0x11, 2)
payload = b'\x00' + struct.pack('B', 0)
ck_a, ck_b = calc_checksum(struct.pack('<BBH', 0x06, 0x11, 2) + payload)
gps_s.write(header + payload + struct.pack('BB', ck_a, ck_b))
print('Done')


def print_buf(b):
    if b.startswith(b'$'):
        print(b.decode('utf-8').strip())
    if b.startswith(b'\xb5'):
        print(hexlify(b).decode('utf-8'))


c = 0
buf = b''
while True:
    char = gps_s.read(1)

    # output buffer when got `$` or `0xb5`
    if char == b'\xb5' or char == b'$':
        print_buf(buf)
        buf = char
    else:
        buf += char

    if c >= 100:
        print('Mem free:', gc.mem_free())
        gc.collect()
        c = 0
        utime.sleep_ms(100)
    c += 1
