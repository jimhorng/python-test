'''
Created on Mar 11, 2014

@author: jimhorng
'''

from apnsclient import apns
import time

AMOUNT = 10
token_hex = '76d1f75c4249efe0cf14af70acef799fd783e561c88e3ca6839f07c913ef646f'
token_hex_bad = '1234575c4249efe0cf14af70acef799fd783e561c88e3ca6839f07c913ef646f'

time_start = time.time()

session = apns.Session()
con_send = session.get_connection("push_sandbox", cert_file="apns.pem")

# message = apns.Message([token_hex_bad], alert="test12333", badge=10)
payload1 = {
    'aps' : {
         'alert' : "test_apns-client",
         'badge' : "999",
         'sound' : 'default'
     },
    'test_key1' : 123,
    'test_key2' : 456
}
# message = apns.Message([token_hex], alert="test12333", badge=10, extra=payload1)

# Send the message.
srv = apns.APNs(con_send)

for i in range(AMOUNT):
    payload1 = {
        'aps' : {
             'alert' : "test_apns-client" + str(i),
             'badge' : "999",
             'sound' : 'default'
         },
        'test_key1' : 123,
        'test_key2' : 456
        }
    message = apns.Message([token_hex_bad], payload=payload1)
    print "before send: ", time.time()
    res = srv.send(message)
    print "after send: ", time.time()
    
    # Check failures. Check codes in APNs reference docs.
    for token, reason in res.failed.items():
        code, errmsg = reason
        print "Device failed: {0}, reason: {1}".format(token, errmsg)
    
    print "after error response: ", time.time()
    
    # Check failures not related to devices.
    for code, errmsg in res.errors:
        print "Error: ", errmsg
    
    # Check if there are tokens that can be retried
    if res.needs_retry():
        retry_message = res.retry()

con_feedback = apns.Session.new_connection("feedback_sandbox", cert_file="apns.pem")
srv = apns.APNs(con_feedback, tail_timeout=10)

# automatically closes connection for you
for token, since in srv.feedback():
    print "Token {0} is unavailable since {1}".format(token, since)

time_end = time.time()
print "time elapsed: ", time_end - time_start

if __name__ == '__main__':
    pass