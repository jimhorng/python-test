'''
Created on Mar 20, 2014

@author: jimhorng
'''

a = [{'id': 1},
     {'id': 2},
     {'id': 3},
     {'id': 4},
     {'id': 5}]

b = [{1: '111'},
     {2: '222'},
     {3: '333'}]

idx = next(index for (index, d) in enumerate(a) if d['id'] == 3)
print idx

print a[idx+1:]
print a
print a[idx+10:]

if __name__ == '__main__':
    pass