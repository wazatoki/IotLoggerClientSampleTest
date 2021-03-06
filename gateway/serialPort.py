import threading
import time
from datetime import datetime
import logging
import random

import serial

from config import config
from gateway import http
from domain import cyclic_data,asynchronous

def create_asynchronous_data():
    a = random.randint(0,100)
    ld = asynchronous.Log_data()
    item = asynchronous.index[a]
    ld.category = item['category']
    ld.code = item['code']
    ld.dt = datetime.now()
    ld.name = item['name']
    return ld    

def create_cyclic_data():

    max = 100
    min = -100
    ld = cyclic_data.Log_data()

    ld.version = 1
    ld.dt = datetime.now()
    a = random.randint(-100,100)
    ld.speed = a
    a = random.randint(-100,100)
    ld.flow = a
    a = random.randint(-100,100)
    ld.pven = a
    a = random.randint(-100,100)
    ld.pint = a
    a = random.randint(-100,100)
    ld.deltap = a
    a = random.randint(-100,100)
    ld.part = a
    a = random.randint(-100,100)
    ld.tven = a
    a = random.randint(-100,100)
    ld.tart = a
    a = random.randint(-100,100)
    ld.svo2 = a
    a = random.randint(-100,100)
    ld.hct = a
    
    return ld

def watch():

    a = random.randint(0,9)

    if a < 2 :
        ld = create_asynchronous_data()
        if ld.name != 'OK':
            http.post_asynchronous(ld.get_Data())
    else:
        ld = create_cyclic_data()
        http.post_cyclic(ld.get_Data())

    t=threading.Timer(2, watch)
    t.start()

def start_watch():
    logging.info('Iot logger client start')
    t=threading.Thread(target=watch)
    t.start()