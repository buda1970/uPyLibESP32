from QUICKCHARGER import *
import time

def main():
    
    quick = QUICKCHARGER()
    quick.set_fix_voltage(9)
    time.sleep(1)
    
    for i in range(50):
        quick.step_200mV_voltage(True)
        time.sleep_ms(100)
        print ('UP', i)
        
    for i in range(60):
        quick.step_200mV_voltage(False)
        time.sleep_ms(100)
        print ('DOWN', i)
    
    print("Welcome to RT-Thread MicroPython!")
    
if __name__ == '__main__':
    main()
    