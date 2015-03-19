'''
Created on Jul 3, 2014

@author: jimhorng
'''

from memory_profiler import profile
import time

@profile
def my_func():
    a = [1] * (10 ** 6)
    b = [2] * (2 * 10 ** 7)
    del b
    time.sleep(100)
    return a

if __name__ == '__main__':
    my_func()