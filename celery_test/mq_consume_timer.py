'''
Created on Feb 24, 2014

@author: jimhorng
'''

import urllib2
import json
import time
from celery_worker_test import QUEUE_NAME

def main():
    print "waiting..."
    print json.dumps({'elapsed_time' : wait_and_get_msg_consuming_time()})

def wait_and_get_msg_consuming_time():
    MSG_QTY = 1
    time_start = time.time()
    while(MSG_QTY != 0):
        time.sleep(1)
        MSG_QTY = get_message_qty_from_default_queue()
    time_end = time.time()
    return int(time_end- time_start)

def get_message_qty_from_default_queue():
    return get_message_qty_from_queue(QUEUE_NAME)

def get_message_qty_from_queue(queue):
    password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
    password_mgr.add_password(None,
                              uri='http://qcloud-dev-mq1:15672/api/',
                              user='guest',
                              passwd='guest')
    # Create an OpenerDirector with support for Basic HTTP Authentication...
    auth_handler = urllib2.HTTPBasicAuthHandler(password_mgr)
    opener = urllib2.build_opener(auth_handler)
    # ...and install it globally so it can be used with urlopen.
    urllib2.install_opener(opener)
    response = urllib2.urlopen('http://qcloud-dev-mq1:15672/api/queues/%2F/' + queue)
    response_json = response.read()
    return json.loads(response_json)['messages']

if __name__ == '__main__':
    main()