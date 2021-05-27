from Logic.AutoChecker import *
import schedule
import time

ac = AutoChecker()


def job():
    print("I'm working...")

schedule.every(3).seconds.do(ac.seekPendingContent)

#schedule.every().day.at("10:30").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)