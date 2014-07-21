'''
Created on Jun 12, 2014

@author: jimhorng
'''
from urllib2 import urlopen

import time

URLS = ["http://www.google.com",
        "http://www.microsoft.com",
        "http://www.facebook.com",
        "http://www.dropbox.com",
        "http://www.twitter.com"]
TASK_NUM = 200

def url_task(url):
    #print('Starting %s' % url)
    data = urlopen(url).read()
    #print('%s: %s bytes: %r' % (url, len(data), data[:50]))

def thread_task():
    from threading import Thread
    threads = []
    for i in xrange(TASK_NUM):
        n = i % len(URLS)
        t = Thread(target=url_task, args=(URLS[n],))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()

def main():
    start = time.time()
    
    thread_task()
#     url_task(url)
    
    print "time used: %f" % (time.time() - start)

if __name__ == '__main__':
    main()