from LEERCFG.LEERCFG import LEERCFG

def main():
    
    print("Operacion con archivos:")
    
    config = LEERCFG('config.cfg')
    print(config.leerConfiguracion('ID'))
    input ('espera: ')
    #config.escribirConfiguracion('ID', '1233')
    print(config.leerConfiguracion('ID'))
    
if __name__ == '__main__':
    main()