'''
Created on Feb 26, 2014

@author: jimhorng
'''

import json
from multiprocessing import Manager

d_proxy = Manager().dict()
d_proxy['test1'] = 123
d_proxy['test2'] = {'foo' : 123}

print type(d_proxy)
print type(d_proxy.items())
print d_proxy['test2']
print type(d_proxy['test2'])

print json.dumps(d_proxy['test2'])
print json.dumps(d_proxy.items())

if __name__ == '__main__':
    pass