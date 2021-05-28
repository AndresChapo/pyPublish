from Logic.AutoChecker import *
import schedule
import time
#import os

#os.system('curl','google.com')

ac = AutoChecker()

#schedule.every(3).seconds.do(ac.seekPendingContent)
schedule.every().day.at("19:00").do(ac.seekPendingContent)
print("Programado desde main.py")

while True:
    print("Chequeando ahora")
    schedule.run_pending()
    time.sleep(3600)

