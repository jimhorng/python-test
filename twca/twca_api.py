'''
Created on Nov 26, 2014

@author: jimhorng
'''
from tornado.httpclient import AsyncHTTPClient
from tornado.httpclient import HTTPRequest
from tornado import ioloop
import json
import time
# from tornado.httputil import url_concat

sent = 0
message_body = "testest_"
base_url = "https://ssl2.twca.com.tw/sslserver/apply"
# ACCESS_TOKEN = 'o0EEHhQoFQeSCXpvN7ZdPqfdEtBjef7iHwf9MGcS'
MSG_QTY = 1
start_time = 0

def handle_request(response):
    if response.error:
        print "Error:", response.error
        print response.body
        pass
    else:
        print response.body
        pass
    global sent
    sent += 1
    if sent >= MSG_QTY:
        ioloop.IOLoop.instance().stop()
        elapsed_time = time.time() - start_time
        print "sent " + str(MSG_QTY) + " msgs in " + str(elapsed_time)


def main():
    # main
    global start_time
    start_time = time.time()
#     AsyncHTTPClient.configure("tornado.curl_httpclient.CurlAsyncHTTPClient")
    http_client = AsyncHTTPClient()
    # full_url = url_concat(base_url)
    headers = {'Authorization': 'Bearer ' + 'test'}
    post_data = {'message': 'test hahah'}
    body = json.dumps(post_data)
    request = HTTPRequest(url=base_url,
                          method='POST',
                          headers=headers,
                          body=body)
    
    for _ in xrange(MSG_QTY):
        http_client.fetch(request, handle_request)
    
    ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()