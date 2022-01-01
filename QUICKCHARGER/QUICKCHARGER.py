import time
from machine import DAC
import machine

class QUICKCHARGER():
    
    VGND    = 0
    V33     = 250
    V06     = 46
    VSETUP  = 128
    
    def __init__(self):
      self.dplus  = DAC(machine.Pin(25))
      self.dminus = DAC(machine.Pin(26))
      self.dplus.write(self.VSETUP)
      time.sleep_ms(1800)
      self.dplus.write(self.V33)
      
   
    def set_fix_voltage(self, voltage):
        
      if voltage == 12:
         self.dplus.write(self.V06)
         self.dminus.write(self.V06)
      elif voltage == 9:
         self.dplus.write(self.V33)
         self.dminus.write(self.V06)
      elif voltage == 20:   
         self.dplus.write(self.V33)
         self.dminus.write(self.V33)
   
    def step_200mV_voltage(self, updown):
      self.dplus.write(self.V06)
      self.dminus.write(self.V33)
      
      if updown:
         self.dplus.write(self.V33)
         time.sleep_ms(1)
         self.dplus.write(self.V06)
      elif not updown :
         self.dminus.write(self.V06)
         time.sleep_ms(1)
         self.dminus.write(self.V33)
      
      self.dplus.write(self.V06)
      self.dminus.write(self.V33)
      
      time.sleep_ms(100)



