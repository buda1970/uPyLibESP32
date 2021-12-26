import usocket as socket
from WIFI import *

def main():
    wifi = WIFI('GatoDumas', 'GatoAnitaKevin!')
    if wifi.conectar(10):
        print('WIFI Conectado')
    else:
        print('WIFI No se conecto')
    
    if wifi.estado():
        
        print('Envio UDP')
        address = ("192.168.1.10", 9997)
        data = b'hello udp'
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        print("data is type {}".format(type(data)))
        sock.sendto(data, address)

        input('intro para continuar TCP')
        data = b'hello tcp'
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("data is type {}".format(type(data)))
        sock.connect(address)
        sock.send(data)
        sock.close()
        
        
        wifi.desconectar()
        print('WIFI Desconectado')

if __name__ == '__main__':
    main()

