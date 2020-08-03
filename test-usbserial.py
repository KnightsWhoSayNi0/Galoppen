#!/usr/bin/env python
import serial
port = "/dev/ttyACM0"

count = 0
s1=serial.Serial(port,9600)
s1.flushInput()

while True:
    tdata =s1.read()
    cdata =tdata.decode("utf-8")
    print(cdata, end = '')
    
    if (cdata=='\n'):
        count = count+1
        print(count)
        
        