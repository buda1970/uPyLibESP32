from GPS import *

def main():
   
   frame = 0
   gps = GPS(2, 115200)
   
   while True:
      if gps.leerPosicion():
         print(gprmc.valido)
         print(gprmc.fecha)
         print(gprmc.hora)
         print(gprmc.latitud)
         print(gprmc.longitud)
         print(gprmc.valido)
         print(gprmc.velocidad)
         print(gprmc.rumbo)
      else:
         print('string invalido. ' + str(frame))
         frame += 1
      utime.sleep(1)
      
   # gprs = GPRMC(strGprs = "$GPRMC,081836,A,3751.65,S,14507.36,E,000.0,360.0,130998,011.3,E*62\n")
   # gprs.gprmc()
   # print(gprs.valido)
   # print(gprs.fecha)
   # print(gprs.hora)
   # print(gprs.latitud)
   # print(gprs.longitud)
   # print(gprs.valido)
   # print(gprs.velocidad)
   # print(gprs.rumbo)
   # print(gprs.onlyGprmc)
   
   del gprs 
    #strGprs = "$GPRMC,081836,A,3751.65,S,14507.36,E,000.0,360.0,130998,011.3,E*62\n"
    #print(isValidGprsStr(strGprs))
    
if __name__ == '__main__':
    main()   