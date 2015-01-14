from tornado.httpclient import AsyncHTTPClient
from tornado.httpclient import HTTPRequest
from tornado import ioloop
import time
# from tornado.httputil import url_concat

sent = 0
message_body = "testest_"
base_url = "http://dev-api.dev-myqnapcloud.com/v1.1/monitor/pair"
ACCESS_TOKEN = 'nJObqYryeVCDgNMyoHwUjnYWPlmg0JYTsasZXBtB'
MSG_QTY = 10000

def handle_request(response):
    if response.error:
#         print "Error:", response.error
#         print response.body
        pass
    else:
#         print response.body
        pass
    global sent
    sent += 1
    if sent >= MSG_QTY:
        ioloop.IOLoop.instance().stop()
        elapsed_time = time.time() - start_time
        print "sent " + str(MSG_QTY) + " msgs in " + str(elapsed_time)

#main
start_time = time.time()
AsyncHTTPClient.configure("tornado.curl_httpclient.CurlAsyncHTTPClient")
http_client = AsyncHTTPClient()
# full_url = url_concat(base_url)
headers={'Authorization': 'Bearer ' + ACCESS_TOKEN}
# headers={}
request = HTTPRequest(url=base_url,
                      headers=headers)

for i in range(MSG_QTY):
    http_client.fetch(request, handle_request)

ioloop.IOLoop.instance().start()