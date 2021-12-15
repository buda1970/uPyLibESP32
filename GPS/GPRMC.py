import utime

class GPRMC():
   
   def __init__(self):
      self.strGprs   = ''
      self.fecha     = '000000'
      self.hora      = '000000'
      self.valido    = 'V'
      self.latSign   = '+'
      self.latitud   = 0.000000
      self.lonSign   = '+'
      self.longitude = 0.000000
      self.velocidad = 0
      self.rumbo     = 0
      self.strGprsOk = False
      self.initStr   = bytes('$PMTK314,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0', 'utf-8')
   
   def gprsStrValido(self):
      
      if self.strGprs[0:6] == bytes('$GPRMC', 'utf-8'):
         
         chkStr = self.strGprs[-3: -1]     
         chksum = 0
         
         for i in self.strGprs[1:]:   #descartar $ inicial y el *. 
            if i != ord('*'):
               #print(chr(i))
               #chksum ^= ord(i)
               chksum ^= i
            else:
               break
         
         #hexa = int('0X' + str(chkStr), 16)
         
         #print(chksum, int(chkStr, 16))
         
         if chksum == int(chkStr, 16):
            self.strGprsOk = True
            return True
         else:
            return False 
      else:
         return False

   def readGprmc(self, strGprs):
      
      self.strGprs = strGprs
      self.stringGprs = self.strGprs.decode()
      #print(type(self.stringGprs))      
      if self.gprsStrValido() == True:
         listaGprmc     = self.stringGprs.split(',')
         self.hora      = listaGprmc[1]
         self.fecha     = listaGprmc[9][-2:] + listaGprmc[9][2:4] + listaGprmc[9][:2]
         self.rumbo     = listaGprmc[8]
         self.velocidad = listaGprmc[7]
         self.latitud   = float(listaGprmc[3])
         if listaGprmc[4].upper() == 'S':
            self.latSign = '-'
         else:
            self.latSign = '+'
         self.longitud   = float(listaGprmc[5])
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
         

         
         