from machine import UART
from GPS.GPRMC import *

class GPS(GPRMC):
   
   def __init__(self, port, baud):
      self.port = port
      self.baud = baud
      global serial
      global gprmc
      
      serial = UART(self.port, self.baud)
      serial.init(baudrate = 115200, bits = 8, parity = None, stop = 1,
               timeout = 100, txbuf = 0, rxbuf = 255, timeout_char = 100)
      
      gprmc = GPRMC()
      serial.write(gprmc.initStr)
      
   def leerPosicion(self):
      try:
         mensaje = serial.readline()
         #mensaje = bytes('$GPRMC,081836,A,3751.65,S,14507.36,E,000.0,360.0,130998,011.3,E*62\n', 'utf-8')
         #print(type(mensaje))
         # if mensaje != '':
         if gprmc.readGprmc(mensaje):
            return True
         else:
            return False
      except:
         return False
      