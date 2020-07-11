import logging
import json

import requests
from pytz import timezone
from config import config

def post_asynchronous(data):

    data['deviceID'] = config.device_id
    data['datetime'] = timezone('Asia/Tokyo').localize(data['datetime']).astimezone(timezone('UTC'))
    data['datetime'] = data['datetime'].strftime('%Y-%m-%dT%H:%M:%S%z')
    print(json.dumps(data))
    response = requests.post(
        'http://'+ config.http_address+':'+config.http_port+'/api/asynchronous/add',
        json.dumps(data),
        headers={'Content-Type': 'application/json'})

    if response.status_code >= 400 and response.status_code < 600 :
        logging.error(response.text)

def post_cyclic(data):

    data['deviceID'] = config.device_id
    data['datetime'] = timezone('Asia/Tokyo').localize(data['datetime']).astimezone(timezone('UTC'))
    data['datetime'] = data['datetime'].strftime('%Y-%m-%dT%H:%M:%S%z')
    print(json.dumps(data))
    response = requests.post(
        'http://'+ config.http_address+':'+config.http_port+'/api/cyclic/add',
        json.dumps(data),
        headers={'Content-Type': 'application/json'})

    if response.status_code >= 400 and response.status_code < 600 :
        logging.error(response.text)