from WIFI.WIFI import WIFI

def main():
    wifi = WIFI('GatoDumas', 'GatoAnitaKevin!')
    if wifi.conectar(10):
        print('WIFI Conectado')
    else:
        print('WIFI No se conecto')
    
    if wifi.estado():
        wifi.desconectar()
        print('WIFI Desconectado')

if __name__ == '__main__':
    main()
