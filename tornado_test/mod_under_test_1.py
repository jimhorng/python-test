'''
Created on Jan 8, 2015

@author: jimhorng
'''

from tornado.gen import coroutine, Return

@coroutine
def _func_under_test():
    temp = yield _func_inner_1()
    raise Return(temp + 1)

@coroutine
def _func_inner_1():
    raise Return(1)

def func_normal_1():
    return 1