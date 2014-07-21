'''
Created on Feb 14, 2014

@author: jimhorng
'''

import celery_worker_test

import string
import random
import json
from multiprocessing import Process, Manager

# Config
MSG_QTY = 3 * 10000
MSG_LENGTH = 1 * 1024
SENDER_QTY = 4

def main():
    global MSG_QTY, SENDER_QTY
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--msg-qty", help="msg quantity", dest='msg_qty', default=MSG_QTY, type=int)
    parser.add_argument("--sender-qty", help="sender quantity", dest='sender_qty', default=SENDER_QTY, type=int)
    args = parser.parse_args()
    MSG_QTY=args.msg_qty
    SENDER_QTY=args.sender_qty
    
    shared_manager = Manager()
    shared_proxy = shared_manager.dict()
    shared_proxy['total_result'] = { 'rate' : 0, 'sent' : 0 }
    
    process_pool = []
    for _ in range(SENDER_QTY):
        p = Process(target=send_msg, args=(shared_proxy,))
        p.start()
        process_pool.append(p)
    
    for process in process_pool:
        process.join()
    
    print json.dumps(shared_proxy['total_result'])

def send_msg(shared_proxy):
    msg = ''.join(random.choice(string.ascii_uppercase) for _ in range(MSG_LENGTH))

    import time
    start = time.time()
    
    for _ in range(MSG_QTY):
        celery_worker_test.test_task3.delay(msg)
    
    time_elapsed = time.time() - start
    rate = int(MSG_QTY / time_elapsed)
#     result = json.dumps({'sent' : MSG_QTY, 'time_elapsed' : time_elapsed, 'rate' : rate})
#     print result
    total_result = shared_proxy['total_result']
    total_result['rate'] += rate
    total_result['sent'] += MSG_QTY
    shared_proxy['total_result'] = total_result

if __name__ == '__main__':
    main()
