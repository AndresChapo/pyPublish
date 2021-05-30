import time
from flask import jsonify

class Logger:
    lista = []

    def __init__(self):
        pass

    def log(self, txt):
        try:
            txt = str(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())) + " - " + txt
            self.lista.append(txt)
            print(txt)
        except:
            print("Se enviaron datos invalidos al log")
            print(txt)

    def toString(self):
        return str(self.lista)

l = Logger()