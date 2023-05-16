import os
import configparser

def loadConfig():
    if os.path.isfile('.conf'):
        config = configparser.ConfigParser()
        config.read('.conf')
        ciudad = config['DEFAULT']['ciudad']
        nombre = config['DEFAULT']['nombre']
        musica = config['DEFAULT']['musica']
        #pais = config['DEFAULT']['pais']
        #noticias = config['DEFAULT']['noticias']
        #topics = config['DEFAULT']['topics']
    else:
        ciudad = input("Introduzca su ciudad:\n")
        nombre = input("Introduzca su nombre:\n")
        musica = input("Introduzca su género músical favorito:\n")
        #pais = input("Introduzca su país:\n")
        #noticias= input("¿Desea que se muestren las noticias de la ciudad? (Si/No):\n")
        #topics = input("Introduzca de entre estos temas los que le insteresan separados por comas: business , entertainment , general , health , science , sports , technology\n")
        config = configparser.ConfigParser()
        config['DEFAULT'] = {'ciudad': ciudad, 'nombre': nombre, 'musica': musica}
        with open('.conf', 'w') as f:
            config.write(f)
    
    settings_list = {"ciudad":ciudad, "nombre":nombre, "musica":musica}    
    return settings_list

if __name__ == "__main__":
    print(loadConfig())