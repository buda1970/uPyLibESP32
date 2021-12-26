from LCD import *
from WIFI import WIFI
from machine import Pin, I2C
import ntptime   #NTP-time (obtenida desde pool.ntp.org)                      
from machine import RTC
import machine
import network
import time

I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

def configurarDisplay(i2c):
    direccion = hex(i2c.scan()[0])
    print('La dirección I2C es ', direccion)
    lcd = I2cLcd(i2c, 0x27, I2C_NUM_ROWS, I2C_NUM_COLS)
    #lcd.putstr("It Works!")
    utime.sleep(2)
    lcd.clear()
    return lcd
    
def blinkLed(led):
    led.on()
    time.sleep_ms(100)
    led.off()
    time.sleep_ms(500)

def main():
    led     = Pin(2, Pin.OUT, Pin.PULL_UP)
    i2c_scl = Pin(22)
    i2c_sda = Pin(21)
    i2c = I2C(scl = i2c_scl, sda = i2c_sda, freq = 400000)
    configurarDisplay(i2c)
    blinkLed(led)

    wifi = WIFI('GatoDumas', 'GatoAnitaKevin!')
    if wifi.conectar(10):
        print('WIFI Conectado')
    else:
        print('WIFI No se conecto')
        
    blinkLed(led)
    
    if wifi.estado():
        ntptime.settime() 
        
        (year, month, mday, weekday, hour, minute, second, milisecond) = RTC().datetime()                
        RTC().init((year, month, mday, weekday, hour - 3, minute, second, milisecond)) 
        
        lcd = configurarDisplay(i2c)
        
        print(year)
        
        while True:
            blinkLed(led)
            print ("Fecha: {:02d}/{:02d}/{:02d}".format(RTC().datetime()[2],
                                                    RTC().datetime()[1],
                                                    RTC().datetime()[0]))

            print ("Hora: {:02d}:{:02d}:{:02d}".format(RTC().datetime()[4],
                                                    RTC().datetime()[5],
                                                    RTC().datetime()[6]))
            
            lcd.putstr("{:02d}/{:02d}/{:04d}".format(RTC().datetime()[2], RTC().datetime()[1], RTC().datetime()[0]))
            lcd.move_to(0, 1)
            lcd.putstr("{:02d}/{:02d}/{:02d}".format(RTC().datetime()[4], RTC().datetime()[5], RTC().datetime()[6]))
                      
            machine.lightsleep(1000)
            lcd.clear()
        
    
if __name__ == '__main__':
    main()