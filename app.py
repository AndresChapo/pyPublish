#import Presentation.main
from Logic.AutoChecker import *
from Logic.Logger import *
from flask import Flask, redirect, url_for, render_template
from time import sleep
from concurrent.futures import ThreadPoolExecutor

config_ini = abrirArchivo('config.ini')
app = Flask(__name__, template_folder="Presentation/templates")
#ambiente = config("AMBIENTE")
app.env = config_ini['AMBIENTE']['env']
app.debug = config_ini['AMBIENTE']['debug']
app.config['FLASK_LOG_LEVEL'] = 'DEBUG'

executor = ThreadPoolExecutor(2)
ac = AutoChecker(config_ini['FRECUENCY']['type'], config_ini['FRECUENCY']['time'], config_ini['FRECUENCY']['sleep_secs'])


@app.route('/start')
def start():
    config_ini = abrirArchivo('config.ini')
    ac.config(config_ini['FRECUENCY']['type'], config_ini['FRECUENCY']['time'],
                     config_ini['FRECUENCY']['sleep_secs'])
    executor.submit(ac.start)
    #executor.submit(some_long_task2, 'hello', 123)
    return redirect('/')

@app.route('/stop')
def stop():
    ac.stop()
    return redirect('/')

def some_long_task2(arg1, arg2):
    l.log("Task #2 started with args: %s %s!" % (arg1, arg2))
    sleep(5)
    l.log("Task #2 is done!")
    redirect('/')

@app.route('/')
def index():

    return render_template('index.html', datos=l.lista)

if __name__ == '__main__':
    app.run()

