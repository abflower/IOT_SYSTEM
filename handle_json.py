import json
import logging
import os

def read_json():
    # Initializes variables to store loaded json files
    data = {}

    # Reads json files and loads data
    json_directory = 'DATA/JSON_FILES'
    checks = 0
    for filename in os.listdir(json_directory):
        f = open(json_directory+'/'+filename) 
        try:
            content = json.load(f)
        except:
            logging.warn('Found file {} but could not load it.'.format(filename))
            checks += 1
            continue
        # assigns content to data under key corresponding to type
        try:
            data[content['type']] = content[content['type']]
            logging.info('Json file -->{}<-- loaded.'.format([content['type']][0]))
        except: 
            checks += 1
            logging.warn('Json file {} is corrupted or uncorrectly loaded.'.format(filename))
            

    return (data, checks)