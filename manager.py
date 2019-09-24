import itertools
import logging
import threading
import time

from automation import automation
from flask import Flask, make_response, render_template, request
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
        return 1
    return 0

def load_automations():
    new_list = []

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
            # adds needed params
            this_automation.extra_params = data['services'][autom['service']]['extra_params']
            # adds automation to list
            new_list.append(this_automation)
        except:
            logging.warn('Error while loading automation: {}.'.format(autom['name']))
    global automations
    automations = new_list

def execute_automations():
    for automation in automations:
        # checks if conditions are satisfied
        try:
            check = globals()[automation.condition_type](**automation.conditions)
                # if so it will execute functions for specific service
            if check > 0:
                try:
                    check_dic = {'check':check}
                    automation.params = {**automation.params, **check_dic}

                    print(globals()[automation.function](**automation.params))
                except:
                    logging.warn('Error when attemping execution of automation: {}.'.format(automation.name))
        except:
            logging.warn('Erroe while checking conditions for automation: {}.'.format(automation.name))
        

### Defines thread class and threads ###

exit_flag_config_thread = 0
exit_flag_automation_thread = 0

class myThread (threading.Thread):
   def __init__(self, threadID, name, function, delay):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.function = function
        self.delay = delay
   def run(self):
        logging.info('Starting thread: ' + self.name)
        #globals()[self.function](*self.delay)    
        self.function(self.delay)   
        logging.info('Exiting thread: ' + self.name)

def read_load_config(delay):
    while True:
        global exit_flag_config_thread
        if exit_flag_config_thread == 0:
            print('read')
            if read_and_check():
                #global exit_flag_config_thread
                exit_flag_config_thread = 1
                global exit_flag_automation_thread
                exit_flag_automation_thread = 1
                break
            else:
                load_automations()
                time.sleep(delay)
        else:
            break

def automations_loop(delay):
    while True:
        if exit_flag_automation_thread == 0:
            print('execute')
            execute_automations()
            time.sleep(delay)
        else:
            break

config_thread = myThread(1, "config_thread", read_load_config, 30)
automation_thread = myThread(2, "automation_thread", automations_loop, 10)


def start():
    config_thread.start()
    automation_thread.start()
    time.sleep(200)
    exit_flag_config_thread = 1
    exit_flag_automation_thread = 1

# read_and_check()
# load_automations()
# execute_automations()

# time.sleep(200)
# exit_flag_config_thread = 1
# exit_flag_automation_thread = 1

start()