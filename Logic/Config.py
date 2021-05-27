from configparser import ConfigParser

def abrirArchivo():
    archivo = '../content.ini'
    # Crear el parser y leer el archivo
    parser = ConfigParser()
    parser.read(archivo)
    return parser

def guardarArchivo(archivo):
    with open('../content.ini', 'w') as archivoini:
        archivo.write(archivoini)

def config(seccion):
    archivo = '../config.ini'
    # Crear el parser y leer el archivo
    parser = ConfigParser()
    parser.read(archivo)

    # Obtener la sección de conexión a la base de datos
    db = {}
    if parser.has_section(seccion):
        params = parser.items(seccion)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Secccion {0} no encontrada en el archivo {1}'.format(seccion, archivo))
    return db

"""
def validar_usuario(usuario, contrasena):
    archivo = 'config.ini'
    parser = ConfigParser()
    parser.read(archivo)
    return (parser.has_section(usuario) and parser[usuario]["password"] == contrasena)

CREDENCIALES_BD = 'PRD_ESCRITURA'

class Credenciales ():

    CREDENCIALES_BD = 'DEMO'
    def credenciales_bd(self):
        return CREDENCIALES_BD
"""