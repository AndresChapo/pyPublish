import time
from Logic.Config import *
from Logic.Publisher import *

class AutoChecker:
    p = Publisher()
    archivo = ""
    configfile = ""

    def __init__(self):
        pass

    def seekPendingContent(self):
        self.configfile = config('PROFILE')
        #self.configfile = Logic.Config.config('ORG_TANDU')
        archivo = abrirArchivo()

        hoy = str(time.gmtime().tm_year) +"-"+str(time.gmtime().tm_mon).zfill(2) +"-"+ str(time.gmtime().tm_mday).zfill(2)
        print("Buscando post para la fecha: "+hoy)

        if archivo.has_section(hoy):
            print("media_category: "+archivo[hoy]['media_category'])
            print("text: "+archivo[hoy]['text'])
            print("published: "+archivo[hoy]['published'])
            if archivo[hoy]['published'] == 'False':
                print(self.p.postProfText(self.configfile['id'], self.configfile['access_token'], archivo[hoy]['text']))
                # print(p.postOrgText(config['id'],config['access_token'], post['text']))
                archivo[hoy]['published'] = 'True'
                guardarArchivo(archivo)
        else:
            print("No hay post para esta fecha: "+hoy)