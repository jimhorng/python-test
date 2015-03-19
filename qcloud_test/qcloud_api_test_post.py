from tornado.httpclient import AsyncHTTPClient
from tornado.httpclient import HTTPRequest
from tornado import ioloop
import json
import time
# from tornado.httputil import url_concat

sent = 0
message_body = "testest_"
base_url = "http://localhost:8080/v1.1/certificate/request"
ACCESS_TOKEN = '2.Ak06J274VFtskGRyMEyJjsOCTJcUE36HlATjRRJU.1425956121'
post_data = {
    "csr" : "MIICtjCCAZ4CAQAwcTELMAkGA1UEBhMCVFcxITAfBgNVBAMMGGFjaGk0NjlwLm15cW5hcGNsb3VkLmNvbTENMAsGA1UEBwwERGFhbjEQMA4GA1UECgwHdGVzdDEyMzEMMAoGA1UECAwDVFBFMRAwDgYDVQQLDAd0ZXN0MTIzMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA3RUqmlAj74Sav5V4KEx9jr48IeJOl9oWkhqRJrIIMfFBHg2IZJGqWS4JEcIeC+kIguk55SSiHVNzDc3EX/6022YwMU6JDaOsmfLuvf8HramgHxC/3owy5qsCMlv80BtCYp1nURNkIlzC9hvrEwa3WAAZ05Bs7Y1hv/4xneiZ8KICXEBsqli56yzBW14VYa1gkaf8byPojVqppUEivZrhzWDReW3QNd8D3e6y6QD2L83NYapJo0Fc4e6Svr8gjgf5O0xDTnhWRgcxbQcXursXID8j9wIEburxDpqC3XNDnzDcdfmrMENfkWSrQFOv1sBA4P85QLu6Ob1PTrBWW6igmwIDAQABoAAwDQYJKoZIhvcNAQELBQADggEBAHGA2SVymXUCJapsuRNDm3M6xEF2Pht1dy4tJf3IU8/64N2YZGjpf8xkKRXd9dfN6agTPzfayMctxmsbke+8iVCpAx2+8RFRuwmgFpxtGMeYtuE9OVmaxJxj4qqiWVtBJBDnz9W54MuZGWyuOQ8yopn8d1rVUy1lrCBVg3RwMB1HTN99dE0L+imzT9Ed37NMGQjPgciaDGhqADpgPD49bomVN8bbhY4JUYldVxGqES2QGWI9XNu6FzNqGYeFG23jOIopmtDuXR8t+ypwsSyaAhzTucI7NzE0bnP2ygGZvNiJQE3jEZC2rvRG5uUWB4yMBRQbBIfMDUKEaXgbVEzNGyw=",
    "device_id" : "53f32a7acc095d45eab1930b",
    "license_id" : "54f56ff8cc095d6de22b821a"
}
MSG_QTY = 10

start_time = None

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
    global start_time
    start_time = time.time()
#     AsyncHTTPClient.configure("tornado.curl_httpclient.CurlAsyncHTTPClient")
    http_client = AsyncHTTPClient()
    # full_url = url_concat(base_url)
    headers = {'Authorization': 'Bearer ' + ACCESS_TOKEN}
    body = json.dumps(post_data)
    request = HTTPRequest(url=base_url,
                          method='POST',
                          headers=headers,
                          body=body)
    
    for i in range(MSG_QTY):
        http_client.fetch(request, handle_request)
    
    ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()