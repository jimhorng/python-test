import time
from tornado import httpclient
from tornado.httputil import url_concat

http_client = httpclient.HTTPClient()

params = {
          "message" : "",
          "regId" : "APA91bG6u48DriQFYqzt6bd_q7ndxLM3HVaIum8-LO-PMWbU8cksPgsFW1VeAUbC23aqQ20VAHoGagHkIW2yGTtk1OW8k1zt6sNCAU_vT5S24tvgD0qyho4INIrheDtAeh1qabMWd5ACUhv5rfsFkcxeLgDmJu_LhLX6uPS0xU0mApmGYTQWs3I",
}
message_body = "testest_"
base_url = "http://192.168.68.108/gcm_server_php/send_message.php"
msg_qty = 10

start_time = time.time()

for i in range(msg_qty):
    try:
        params["message"] = message_body + str(i + 1)
        full_url = url_concat(base_url, params)
        response = http_client.fetch(httpclient.HTTPRequest(full_url, method="GET"))
        #print response.body
    except httpclient.HTTPError as e:
        print "Error:", e


http_client.close()

elapsed_time = time.time() - start_time
print "sent " + str(msg_qty) + " msgs in " + str(elapsed_time)
