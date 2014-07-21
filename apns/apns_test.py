'''
Created on Mar 10, 2014

@author: jimhorng
'''

from apns import APNs, Payload
import time
import logging
import sys
import random

# Configurations
SEND_INTERNAL=0.01
# TOKEN_HEX = '76d1f75c4249efe0cf14af70acef799fd783e561c88e3ca6839f07c913ef646f' #ipad test app
# TOKEN_HEX = '2d5ba485e86cddfd5e9577f1de0b701708792f73b1324eb4960c6e7e963d1675' #Hades
TOKEN_HEX = '9094df9641afb864c4145a61b10e1777ca141bab3d72d75eb78354211c5f8a9f' #Alpha qmanager

TOKEN_HEX_BAD = '123457894249efe0cf14af70acef799fd783e561c88e3ca6839f07c913ef6412'

# CERT_FILE = 'apns_qnap_dev.pem'
# CERT_FILE = 'apns_enterprise_dist.pem'
# CERT_FILE = 'apns_bad.pem'
CERT_FILE = 'Qmanager_Enterprise_Distribution.pem'

USE_SANDBOX=False

_logger = logging.getLogger()
stream_handler = logging.StreamHandler(stream=sys.stdout)
formatter = logging.Formatter('[%(asctime)s][%(process)s][%(threadName)s][%(pathname)s:%(lineno)d][%(levelname)s] %(message)s','%m-%d %H:%M:%S')
stream_handler.setFormatter(formatter)
_logger.addHandler(stream_handler)
_logger.addHandler(logging.FileHandler(filename='log'))
_logger.setLevel(logging.DEBUG)

apns = APNs(use_sandbox=USE_SANDBOX, cert_file=CERT_FILE, enhanced=True)

import datetime
payload123 = {'aps': {
                   'badge': 9,
                   'alert': "jim:apns_test 123 " + str(datetime.datetime.now().isoformat()),
                   'sound': "default"
                   },
              'test_key1': "test123"
    }

def response_listener(error_response):
    _logger.debug("client get error-response: " + str(error_response))

def wait_till_error_response_unchanged():
    if hasattr(apns.gateway_server, '_is_resending'):
        delay=1
        count = 0
        while True:
            if apns.gateway_server._is_resending == False:
                time.sleep(delay)
                if apns.gateway_server._is_resending == False:
                    count = count + delay
                else: count = 0
            else: count = 0
            
            if count >= 10:
                break
        return delay * count
    return 0

def process(token, qty):
    payload = payload123.copy()
    base_alert = payload123['aps']['alert']
    for i in range(1, qty+1):
        payload['aps']['alert'] = base_alert + str(i)
#         identifier = random.getrandbits(32)
        identifier = i
        time.sleep(SEND_INTERNAL)
        apns.gateway_server.register_response_listener(response_listener)
        apns.gateway_server.send_notification(token, Payload(custom=payload), identifier=identifier)
        _logger.info("client sent to: " + str(identifier))
    
    for (token, failed_time) in apns.feedback_server.items():
        _logger.debug("failed: " + str(token) + "\tmsg: " + str(failed_time))

def test_random_identifier(qty):
    payload = payload123.copy()
    for _ in range(qty):
        identifier = random.getrandbits(32)
        apns.gateway_server.send_notification(TOKEN_HEX, Payload(custom=payload), identifier=identifier)
        print "sent to ", identifier

def test_normal_fail():
    payload = payload123.copy()
    identifier = 1
    alert_content = payload['aps']['alert']
    payload['aps']['alert'] = alert_content + str(identifier)
    apns_response = apns.gateway_server.send_notification(TOKEN_HEX, Payload(custom=payload), identifier=identifier)
    print "sent test_normal to: ", identifier, "\tresponse: ", apns_response
    identifier += 1
    payload['aps']['alert'] = alert_content + str(identifier)
    apns_response = apns.gateway_server.send_notification(TOKEN_HEX, Payload(custom=payload), identifier=identifier)
    print "sent test_normal to: ", identifier, "\tresponse: ", apns_response
    identifier += 1
    payload['aps']['alert'] = alert_content + str(identifier)
    apns_response = apns.gateway_server.send_notification(TOKEN_HEX_BAD, Payload(custom=payload), identifier=identifier)
    print "sent test_fail to: ", identifier, "\tresponse: ", apns_response
    identifier += 1
    payload['aps']['alert'] = alert_content + str(identifier)
    apns_response = apns.gateway_server.send_notification(TOKEN_HEX, Payload(custom=payload), identifier=identifier)
    print "sent test_normal to: ", identifier, "\tresponse: ", apns_response
    identifier += 1
    payload['aps']['alert'] = alert_content + str(identifier)
    apns_response = apns.gateway_server.send_notification(TOKEN_HEX, Payload(custom=payload), identifier=identifier)
    print "sent test_normal to: ", identifier, "\tresponse: ", apns_response
    
def test_normal(qty=1):
    process(TOKEN_HEX, qty=qty)

def test_fail(qty):
    process(TOKEN_HEX_BAD, qty=qty)

def test_fail_nonenhance(qty):
    global apns
    apns = APNs(use_sandbox=True, cert_file=CERT_FILE)
    process(TOKEN_HEX_BAD, qty=qty)

def test_normal_nonenhance(qty):
    global apns
    apns = APNs(use_sandbox=True, cert_file=CERT_FILE)
    process(TOKEN_HEX, qty=qty)

def test_send_interval():
    for _ in xrange(100):
        test_normal(5)
        time.sleep(10)

def test_send_by_signal():
    import signal
    signal.signal(signal.SIGUSR2, sig_handler_for_test_normal)
    
    while True:
        time.sleep(1)

def sig_handler_for_test_normal(signum, frame):
    _logger.debug('Signal handler called with signal:%s' % signum)
    import traceback
    _logger.debug("trackback:%s" % traceback.format_stack(frame))
    test_normal(2)

def test_runner():
#     test_normal(1)
#     test_normal_fail()
#     test_fail(10)
#     test_fail_nonenhance(100)
#     test_normal_nonenhance(100)
#     test_random_identifier(1000)
#     test_send_interval()
    test_send_by_signal()

def main():
#     time_start = time.time()
    
    test_runner()
    
    time.sleep(60)
    
#     delay = wait_till_error_response_unchanged()
    apns.gateway_server.close_read_thread()
#     time_end = time.time()
#     _logger.info("time elapsed: " + str(time_end - time_start - delay))
    
if __name__ == '__main__':
    main()