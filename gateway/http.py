import logging
import json

import requests

from config import config

def post_asynchronous(data):

    data.device_id = config.device_id
    response = requests.post(
        'http://'+ config.http_address+':'+config.http_port+'/asynchronous',
        json.dumps(data),
        headers={'Content-Type': 'application/json'})

    if response.status_code >= 400 and response.status_code < 600 :
        logging.error(response.text)

def post_cyclic(data):

    data.device_id = config.device_id
    response = requests.post(
        'http://'+ config.http_address+':'+config.http_port+'/cyclic',
        json.dumps(data),
        headers={'Content-Type': 'application/json'})

    if response.status_code >= 400 and response.status_code < 600 :
        logging.error(response.text)