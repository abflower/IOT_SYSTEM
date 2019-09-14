import itertools
import logging
import time
from automation import automation
from handle_json import read_json
from services import *

# set loging
logging.basicConfig(filename='manager.log',level=logging.DEBUG,format='%(asctime)s %(levelname)s %(message)s')

data = ''
automations = []


def read_and_check():
    logging.info('Now reading json files.')
    # reads json file and loads them 
    readind_data = read_json()
    global data
    data = readind_data[0]
    # checks if some error has occurred while loading
    if readind_data[1] > 0:
        logging.warn('Some error occurred while reading json files.')


def load_automations():
    for autom in data['automations']:
        # retrieves service
        service = data['services'][autom['service']]
        # compiles parameters
        params = {**service['params'], **autom['params']}
        print(params)
        automations.append(automation(autom['id'], autom['name'], service['function'], params))


def execute_automations():
    for automation in data['automations']:
        # retrieves service
        service = data['services'][automation['service']]
        # compiles parameters
        params = {**service['params'], **automation['params']}
        #print(params)
        print(globals()[service['function']](**params))


read_and_check()
#execute_automations()
load_automations()
for aut in automations:
    aut.print_all_attrs()

#automations.append(automation(1,'tarapia'))
#print(automations)