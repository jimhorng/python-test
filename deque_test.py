'''
Created on Mar 25, 2014

@author: jimhorng
'''

import collections, itertools

dq = collections.deque(maxlen=10)

for i in range(12):
#     if len(dq) >= dq.maxlen:
#         dq.popleft()
    dq.append({'id': i, 'data': "haha"})

dq.popleft()
dq.popleft()

print collections.deque(itertools.islice(dq, 4, len(dq)))

print collections.deque(itertools.islice(dq, 11, 12))

first = len(dq) - 10 if len(dq) >= 10 else 0
print collections.deque(itertools.islice(dq, first, len(dq)))

print dq

print next(index for (index, d) in enumerate(dq) 
                        if d['id'] == 8)

if __name__ == '__main__':
    pass