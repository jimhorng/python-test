from tornado.httpclient import AsyncHTTPClient
from tornado import ioloop
import time
from tornado.httputil import url_concat

sent = 0
params = {
          "message" : "",
          "regId" : "APA91bG6u48DriQFYqzt6bd_q7ndxLM3HVaIum8-LO-PMWbU8cksPgsFW1VeAUbC23aqQ20VAHoGagHkIW2yGTtk1OW8k1zt6sNCAU_vT5S24tvgD0qyho4INIrheDtAeh1qabMWd5ACUhv5rfsFkcxeLgDmJu_LhLX6uPS0xU0mApmGYTQWs3I",
}
message_body = "testest_"
base_url = "http://localhost/gcm_server_php/send_message.php"
msg_qty = 110

def handle_request(response):
    if response.error:
        print "Error:", response.error
    else:
        print response.body
        pass
    global sent
    sent += 1
    if sent >= msg_qty:
        ioloop.IOLoop.instance().stop()
        elapsed_time = time.time() - start_time
        print "sent " + str(msg_qty) + " msgs in " + str(elapsed_time)

http_client = AsyncHTTPClient()
start_time = time.time()

for i in range(msg_qty):
    params["message"] = message_body + str(i + 1)
    full_url = url_concat(base_url, params)
    http_client.fetch(full_url, handle_request)

ioloop.IOLoop.instance().start()