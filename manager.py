import flask
import itertools
import logging
import time
from automation import automation
from flask import Flask, make_response, render_template, request
from handle_json import read_json
from services import *
from conditions import *

# set logging
logging.basicConfig(filename='manager.log',level=logging.WARNING,format='%(asctime)s %(levelname)s %(message)s')

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
            # adds needed params
            this_automation.extra_params = data['services'][autom['service']]['extra_params']
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

###### FLASK ######
app = Flask(__name__)

@app.route('/')
def index():
    return '''HOME</br>
    <a href="/autom_list">List of automations</a>'''

@app.route('/autom_list')
def autom_list():
    text = '<p>List of automations</p><ul>'
    for automation in automations:
        text += '<li><a href="/autom_page?id={}">{}</a></li>'.format(automation.id, automation.name)
    text += '</ul><a href="/">Home</a>'
    return text
    # return 'booo'

@app.route('/autom_page')
def autom_page():
    id = request.args.get('id')
    response=''
    for automation in automations:
        if automation.id == id:
            info = automation.return_all_attrs()
            service_fields = []
            for param in automation.extra_params:
                field = {}
                field['name'] = param['name']
                field['value'] = automation.params[param['name']]
                service_fields.append(field)
            conditions_list = []
            for key in automation.conditions.keys():
                field = {}
                field['name'] = key
                field['value'] = automation.conditions[key]
                conditions_list.append(field)

            response = make_response(render_template("single_service.html", info=info, service_fields=service_fields, conditions_list=conditions_list))
    return response


if __name__ == '__main__':
    app.run(debug=True)
