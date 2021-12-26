from NEO9 import *

def main():
   valido    = 'A'
   fecha     = '980913'
   hora      = '081836'
   latSign   = '-'
   latitud   = 751.65
   longSign  = '-'
   longitud  = 4507.36
   velocidad = 000
   rumbo     = 90
   id        = '1234'
   evento    = '10'
   
   neo = NEO9()
   print(neo.strSalida(fecha, hora, latSign, latitud, longSign, longitud, \
         valido, velocidad, rumbo, evento, id))
   
   
if __name__ == '__main__':
   main()
   
      
   