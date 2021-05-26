import time
import Logic.Config
#import Logic.Publisher
from Logic.Publisher import *

p = Publisher()
archivo = ""
config = Logic.Config.config('PROFILE')
#config = Logic.Config.config('ORG_TANDU')
archivo = Logic.Config.abrirArchivo()

hoy = str(time.gmtime().tm_year) +"-"+str(time.gmtime().tm_mon).zfill(2) +"-"+ str(time.gmtime().tm_mday).zfill(2)
print("Buscando post para la fecha: "+hoy)

if archivo.has_section(hoy):
    print("media_category: "+archivo[hoy]['media_category'])
    print("text: "+archivo[hoy]['text'])
    print("published: "+archivo[hoy]['published'])
    if archivo[hoy]['published'] == 'False':
        print(p.postProfText(config['id'], config['access_token'], archivo[hoy]['text']))
        # print(p.postOrgText(config['id'],config['access_token'], post['text']))
        archivo[hoy]['published'] = 'True'
        Logic.Config.guardarArchivo(archivo)
else:
    print("No hay post para esta fecha: "+hoy)



