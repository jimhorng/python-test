'''
Created on Jul 21, 2014

@author: jimhorng
'''

from tornado import ioloop
import time

time_start = time.time()

def main():
    callback_task = ioloop.PeriodicCallback(callback1, 2000, ioloop.IOLoop.instance())
    callback_task.start()
    ioloop.IOLoop.instance().start()
    print "ioloop started"
    time.sleep(30)
    print "after 30 secs"

def callback1():
    print("time elapsed: %s" % str(time.time() - time_start))
    
if __name__ == '__main__':
    main()