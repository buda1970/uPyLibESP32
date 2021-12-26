
from machine import Pin, I2C
import utime
from LCD import *

I2C_NUM_ROWS = 4
I2C_NUM_COLS = 16

def main():
   
   led     = Pin(2, Pin.OUT, Pin.PULL_UP)
   i2c_scl = Pin(22)
   i2c_sda = Pin(21)
   i2c = I2C(scl = i2c_scl, sda = i2c_sda, freq = 400000)
   #i2c = SoftI2C(scl = Pin(22), sda = Pin(21), freq = 100000) 
   direccion = hex(i2c.scan()[0])
   print('La dirección I2C es ', direccion)
   
   lcd = I2cLcd(i2c, 0x27, I2C_NUM_ROWS, I2C_NUM_COLS)
   lcd.putstr("It Works!")
   utime.sleep(2)
   lcd.clear()
   count = 0
  
   while True:
      led.on()
      lcd.clear()
      time = utime.localtime()
      lcd.putstr("{year:>04d}/{month:>02d}/{day:>02d} {HH:>02d}:{MM:>02d}:{SS:>02d}".format(
         year=time[0], month=time[1], day=time[2],
         HH=time[3], MM=time[4], SS=time[5]))
      if count % 10 == 0:
         print("Turning cursor on")
         lcd.show_cursor()
      if count % 10 == 1:
         print("Turning cursor off")
         lcd.hide_cursor()
      if count % 10 == 2:
         print("Turning blink cursor on")
         lcd.blink_cursor_on()
      if count % 10 == 3:
         print("Turning blink cursor off")
         lcd.blink_cursor_off()                    
      if count % 10 == 4:
         print("Turning backlight off")
         lcd.backlight_off()
      if count % 10 == 5:
         print("Turning backlight on")
         lcd.backlight_on()
      if count % 10 == 6:
         print("Turning display off")
         lcd.display_off()
      if count % 10 == 7:
         print("Turning display on")
         lcd.display_on()
      if count % 10 == 8:
         print("Filling display")
         lcd.clear()
         string = ""
         for x in range(32, 32 + I2C_NUM_ROWS * I2C_NUM_COLS):
               string += chr(x)
         lcd.putstr(string)
      count += 1
      utime.sleep(1)
      led.off()
      utime.sleep(1)
   
if __name__ == '__main__':
   main()
   