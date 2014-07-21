'''
Created on Jun 12, 2014

@author: jimhorng
'''
import gevent
# from gevent import socket
from gevent import monkey; monkey.patch_socket()
from urllib2 import urlopen

import time

URL = "http://www.google.com.tw"
# URLS = ["http://abc.go.com/",
#         "http://www.nba.com",
#         "http://zh.wikipedia.org/",
#         "http://www.tvbs.com.tw/",
#         "http://www.ltn.com.tw/"]

URLS = ["http://abc.go.com/"]

TASK_NUM = 2000

task_seq = []

def check_task_seq():
    print "checking task seq..."
    for i, seq in enumerate(task_seq):
        if i != seq:
            print ("ERROR: i:%s != seq:%s" % (i, seq) )

def url_task():
    #print('Starting %s' % url)
    urlopen(URL).read()
    #print('%s: %s bytes: %r' % (url, len(data), data[:50]))

def url_task2(task=0):
#     gevent.sleep(0.05)
    task_seq.append(task)
    for i, url in enumerate(URLS):
        print "[%s, %s] opening: %s: %s" % (gevent.getcurrent(), task, i, url)
        urlopen(url).read()

def cpu_task():
    for _ in xrange(1000000):
        i = 1
        i += 1
        i -= 1

def gevent_task(task):
    jobs = [gevent.spawn(task, i) for i in xrange(TASK_NUM)]
    gevent.wait(jobs)

def thread_task(task):
    from threading import Thread
    threads = []
    for _ in xrange(TASK_NUM):
        t = Thread(target=task)
        t.start()
        threads.append(t)
    for t in threads:
        t.join()

def one_thread(task):
    for _ in xrange(TASK_NUM):
        task()

def main():
    start = time.time()
    
    gevent_task(url_task2)
#     gevent_task(cpu_task)
#     thread_task(cpu_task)
#     one_thread(url_task)
    check_task_seq()
    
    print "time used: %f" % (time.time() - start)

if __name__ == '__main__':
    main()