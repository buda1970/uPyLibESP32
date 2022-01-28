from machine import UART
import utime

class GPS():
   
   def __init__(self, port, baud):
      self.strGprmc  = ''
      self.fecha     = ''
      self.hora      = 0
      self.valido    = 'V'
      self.latSign   = '+'
      self.latitud   = 0.000000
      self.lonSign   = '+'
      self.longitude = 0.000000
      self.velocidad = 0
      self.rumbo     = 0
      self.strGprmcOk = False
      self.initStr   = bytes('$PMTK314,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0*29', 'utf-8')
      self.gpsMode   = bytes('$PMTK353,1,0,0,0,0*2A', 'utf-8')
   
      self.port = port
      self.baud = baud
      
      self.serial = UART(self.port, self.baud)
      self.serial.init(baudrate = self.baud, bits = 8, parity = None, stop = 1,
               timeout = 100, txbuf = 0, rxbuf = 255, timeout_char = 100)
      
      utime.sleep(1)
      self.serial.write(self.initStr)
      self.serial.write(b'\x0D\x0A')
      # serial.write(chr(0x0D))
      # serial.write(chr(0x0A))
      utime.sleep(1)
      
      #self.serial.write(self.gpsMode)
      # serial.write(chr(0x0D))
      # serial.write(chr(0x0A))
      #self.serial.write(b'\x0D\x0A')
      
   def __del__(self):
      pass
   
   def gprmcStrValido(self):
      if self.strGprmc[3:6] == bytes('RMC', 'utf-8'):
         chkStr = self.strGprmc[-4: -1]     
         chksum = 0
         #print(chksum, int(chkStr, 16))
         
         for i in self.strGprmc[1:]:   #descartar $ inicial y el *. 
            if i != ord('*'):
               chksum ^= i
            else:
               break
         if chksum == int(chkStr, 16):
            self.strGprmcOk = True
            return True
         else:
            return False 
      else:
         return False

   def readGprmc(self, strGprmc):
      
      self.strGprmc = strGprmc
      self.stringGprmc = self.strGprmc.decode('UTF-8')
      
      #print(type(self.stringGprs))      
      #print(self.stringGprmc) 
      
      if self.gprmcStrValido():
         
         listaGprmc = self.stringGprmc.split(',')
         
         try:
            self.hora = float(listaGprmc[1])
         except:
            self.hora = 0
            
         self.fecha     = listaGprmc[9][-2:] + listaGprmc[9][2:4] + listaGprmc[9][:2]
         try:
            self.rumbo = int(listaGprmc[8])
         except:
            self.rumbo = 0
         
         try:
            self.velocidad = float(listaGprmc[7])
         except:
            self.velocidad = 0
         
         try:
            self.latitud   = float(listaGprmc[3])
         except:
            self.latitud   = float(0)
         
         if listaGprmc[4].upper() == 'S':
            self.latSign = '-'
         else:
            self.latSign = '+'
            
         try:
            self.longitud   = float(listaGprmc[5])
         except:
            self.longitud   = float(0)
         
         if listaGprmc[6].upper() == 'W':
            self.lonsign = '-'
         else:
            self.lonsign = '+'
            
         if listaGprmc[2].upper() == 'A':
            self.valido = 'A'
         else:
            self.valido = 'V'
            
         return True
      else:
         return False
      
   def nmea2decimal(self, nmea):
      unidad = int(nmea / 100)
      decimal = (nmea - unidad * 100) / 60
      return (unidad + decimal)
   
   def leerPosicion(self):
      try:
         mensaje = self.serial.readline()
         #mensaje = bytes('$GPRMC,081836,A,3751.65,S,14507.36,E,000.0,360.0,130998,011.3,E*62\n', 'utf-8')
         print(mensaje)
         if self.readGprmc(mensaje):
            return True
         else:
            print("Error al decodificar la linea")  
            return False
      except:
         print("Error al leer la linea") 
         return False
