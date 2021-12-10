class NEO9():
   
   def __init__(self):
      'fecha: '
      self.fecha     = '000000'
      self.hora      = '000000'
      self.latSign   ='+'
      self.latitud   = '0000.0000'
      self.lonSign   ='+'
      self.longitud  = '00000.0000'
      self.validez   = '0'
      self.velocidad = '000'
      self.rumbo     = '000'
      self.id        = '0000'
      self.contador  = 0
   
   def chksum(salida):
      chk = 0
      
      for i in salida:  
         chk ^= i
      return chk
           
   def strSalida(self, fecha, hora, latSign, latitud, lonSign, longitud, \
                 validez, velocidad, rumbo, evento, id):
      self.fecha     = fecha
      self.hora      = hora
      self.latSign   = latSign
      self.latitud   = latitud
      self.lonSign   = lonSign
      self.longitud  = longitud
      self.validez   = validez
      self.velocidad = velocidad
      self.rumbo     = rumbo
      self.id        = id
      self.contador  += 1
      
      salida = bytes('>RGP' + self.fecha + self.hora + \
               self.latSign + "{:09.4f}".format(self.latitud) + \
               self.lonSign + "{:010.4f}".format(self.longitud) + \
               "{:03d}".format(self.velocidad) + \
               "{:03d}".format(self.rumbo) + \
               self.validez + '000001;&%'  + evento + ';' + \
               'ID=' + self.id + ';#%' + "{:04d}".format(self.contador) + '*', 'utf-8')      

      
      chksum = 0
      for i in salida:  
         chksum ^= i
         
      #print(hex(chksum))
      
      chkStr = hex(chksum).upper()
      
      salida = salida + chkStr[2:] + '<'
      return salida
   
   