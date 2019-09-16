import itertools
import logging
import time
from automation import automation
from handle_json import read_json
from services import *
from conditions import *

# set logging
logging.basicConfig(filename='manager.log',level=logging.DEBUG,format='%(asctime)s %(levelname)s %(message)s')

data = ''
automations = []


def read_and_check():
    logging.info('Now reading json files.')
    # reads json file and loads them 
    reading_data = read_json()
    global data
    data = reading_data[0]
    # checks if some error has occurred while loading
    if reading_data[1] > 0:
        logging.warn('Error while reading json files.')

def load_automations():
    for autom in data['automations']:
        try:
            # retrieves service
            service = data['services'][autom['service']]
            # creates automation object
            this_automation = automation(**autom)
            # adds name of function for service
            this_automation.function = data['services'][autom['service']]['function']
            # merges automation and service parameters
            this_automation.params = {**this_automation.params, **service['params']}
            # adds automation to list
            automations.append(this_automation)
        except:
            logging.warn('Error while loading automation: {}.'.format(autom['name']))

def execute_automations():
    for automation in automations:
        # checks if conditions are satisfied
        try:
            if (globals()[automation.condition_type](**automation.conditions)):
                # if so it will execute functions for specific service
                try:
                    print(globals()[automation.function](**automation.params))
                except:
                    logging.warn('Error when attemping execution of automation: {}.'.format(automation.name))
        except:
            logging.warn('Erroe while checking conditions for automation: {}.'.format(automation.name))
        
read_and_check()
load_automations()
execute_automations()

