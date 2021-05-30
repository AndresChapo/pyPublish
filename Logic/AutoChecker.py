import time
import schedule
from Logic.Config import *
from Logic.Publisher import *
from Logic.Logger import *

class AutoChecker:
    p = Publisher()
    archivo = ""
    configfile = ""
    type=""
    time=1
    sleep_secs=1
    running=False

    def __init__(self,type,time,sleep_secs):
        self.config(type,time,sleep_secs)

    def config(self,type,time,sleep_secs):
        self.configfile = config('PROFILE')
        self.type = type
        self.time = time
        self.sleep_secs = sleep_secs
        """
        if type == 'SECONDS':
            schedule.every(int(time)).seconds.do(self.seekPendingContent)
        if type == 'HOUR':
            schedule.every().day.at(str(time)).do(self.seekPendingContent)
        """
    def seekPendingContent(self):
        #self.configfile = Logic.Config.config('ORG_TANDU')
        archivo = abrirArchivo('content.ini')

        #hoy = str(time.gmtime().tm_year) +"-"+str(time.gmtime().tm_mon).zfill(2) +"-"+ str(time.gmtime().tm_mday).zfill(2)
        hoy = str(time.strftime("%Y-%m-%d %H", time.gmtime()))
        l.log("Buscando post para la fecha: " + hoy)

        if archivo.has_section(hoy):
            l.log("media_category: "+archivo[hoy]['media_category'])
            l.log("text: "+archivo[hoy]['text'])
            l.log("published: "+archivo[hoy]['published'])

            if archivo[hoy]['published'] == 'False':
                l.log(str(self.p.postProfText(self.configfile['id'], self.configfile['access_token'], archivo[hoy]['text'])))
                # l.log(p.postOrgText(config['id'],config['access_token'], post['text']))
                archivo[hoy]['published'] = 'True'
                guardarArchivo(archivo)
        else:
            l.log("No hay post para esta fecha: "+hoy)


    def start(self):
        l.log("AutoChecker start")
        l.log("Type: " + self.type)
        l.log("Time: " + str(self.time))
        l.log("sleep_secs: " + str(self.sleep_secs))
        self.running = True
        while self.running==True:
            l.log("Chequeando ahora")
            #schedule.run_pending()
            self.seekPendingContent()
            time.sleep(int(self.sleep_secs))
        l.log("Se detuvo AutoCheck")

    def getSettings(self):
        return self.type, self.time

    def stop(self):
        l.log("Deteniendo proceso")
        self.running = False