import network
import time

class WIFI():
    
    def __init__(self, ssid, password):
        self.ssid = ssid
        self.password = password
        self.station = network.WLAN(network.STA_IF)
        
    def conectar(self, timeout):
        contador = timeout
        #station = network.WLAN(network.STA_IF)
        if self.station.isconnected():    
            return True
        else:
            self.station.active(True)
            self.station.connect(self.ssid, self.password)
            while (self.station.isconnected() == False) & (contador > 1):
                time.sleep(1)
                contador -= 1
            
            if self.station.isconnected():    
                return True
            else:
                return False

    def desconectar(self):
        if self.station.isconnected():    
            self.station.disconnect()
            
    def estado(self):
        return self.station.isconnected()

