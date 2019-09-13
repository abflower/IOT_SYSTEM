import itertools
import logging
import time
from handle_json import read_json
from services import *

# set loging
logging.basicConfig(filename='manager.log',level=logging.DEBUG,format='%(asctime)s %(levelname)s %(message)s')

data = ''

def read_and_check():
    logging.info('Now reading json files.')
    # reads json file and loads them 
    readind_data = read_json()
    global data
    data = readind_data[0]
    # checks if some error has occurred while loading
    if readind_data[1] > 0:
        logging.warn('Some error occurred while reading json files.')


def execute_automations():
    for automation in data['automations']:
        # retrieves service
        service = data['services'][automation['service']]
        # compiles parameters
        params = {**service['params'], **automation['params']}
        #print(params)
        print(globals()[service['function']](**params))



read_and_check()
execute_automations()