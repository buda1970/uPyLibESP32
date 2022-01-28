from GPS import *

def main():
   
   frame = 0
   gps = GPS(2, 9600)
   
   while True:
     
      if gps.leerPosicion() == True:
         print('string: ' + str(frame))
         print(gps.valido)
         print(gps.fecha)
         print(gps.hora)
         print(gps.latitud)
         print(gps.longitud)
         print(gps.velocidad)
         print(gps.rumbo)
         
         latitud  = gps.nmea2decimal(gps.latitud)
         longitud = gps.nmea2decimal(gps.longitud)
                  
         if gps.valido == 'A':
            if gps.latSign == '-':
               latitud = -latitud
               pass
            
            if gps.lonsign == '-':
               longitud = -longitud
               pass
            
            print(latitud, longitud)
            
      else:
         print('string invalido. ' + str(frame))
         
      frame += 1   
      utime.sleep(1)
   
   del gps 
    #strGprs = "$GPRMC,081836,A,3751.65,S,14507.36,E,000.0,360.0,130998,011.3,E*62\n"
    #print(isValidGprsStr(strGprs))
    
if __name__ == '__main__':
    main()   