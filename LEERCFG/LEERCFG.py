import json

class LEERCFG():
    
    def __init__(self, archivo):
        self.archivo = archivo
        
        try:
            with open(self.archivo, 'r') as self.config:
                self.configuracion = json.load(self.config)
        except:
            print('crear archivo ' + self.archivo)
            formateo = {"ID"        : "1234", \
                        "Intervalo" : 0,      \
                        "Minimo"    : 0,      \
                        "Maximo"    : 0}
            
            with open(self.archivo, 'w') as self.config:
                json.dump(formateo, self.config)
            self.config.close()
                
            with open(self.archivo, 'r') as self.config:
                self.configuracion = json.load(self.config)
        
    def leerConfiguracion(self, item):
        return self.configuracion[item] 
    
    def escribirConfiguracion(self, item, valor):
        self.configuracion[item] = valor
        self.config.close()
        
        with open(self.archivo, 'w') as self.config:
                json.dump(self.configuracion, self.config)
        