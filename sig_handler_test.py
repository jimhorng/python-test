'''
Created on Mar 10, 2015

@author: jimhorng
'''

def goodbye():
    print 'Goodbye...'

import atexit
atexit.register(goodbye)

import time
time.sleep(100)