import time
import Logic.Config
#import Logic.Publisher
from Logic.Publisher import *

p = Publisher()

#config = Logic.Config.config('PROFILE')
config = Logic.Config.config('ORG_TANDU')

print(config['id'])
print(config['access_token'])

#print(p.postProfText(config['id'],config['access_token'],"Hola mundo"))
print(p.postOrgText(config['id'],config['access_token'],"Hola mundo"))

print(time.ctime())
print(time.gmtime())