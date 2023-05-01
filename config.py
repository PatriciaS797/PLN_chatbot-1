import os
import configparser

def loadConfig():
    if os.path.isfile('.conf'):
        config = configparser.ConfigParser()
        config.read('.conf')
        ciudad = config['DEFAULT']['ciudad']
        nombre = config['DEFAULT']['nombre']
    else:
        ciudad = input("Introduzca su ciudad:\n")
        nombre = input("Introduzca su nombre:\n")
        config = configparser.ConfigParser()
        config['DEFAULT'] = {'ciudad': ciudad, 'nombre': nombre}
        with open('.conf', 'w') as f:
            config.write(f)
    
    settings_list = {"ciudad":ciudad, "nombre":nombre}    
    return settings_list

if __name__ == "__main__":
    print(loadConfig())