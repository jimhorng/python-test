DATA = {
    'a' : "AAA",
    'b' : {
         'c' : "AAA",
         'd' : "DDD",
         'e' : {
              'f' : "BBB",
              'g' : "AAA"
         }
    }
}

import collections

def update(d, u):
    for k, v in u.iteritems():
        if isinstance(v, collections.Mapping):
            r = update(d.get(k, {}), v)
            d[k] = r
        else:
            d[k] = u[k]
    return d

def print_dict(d):
    for k, v in d.iteritems():
        if isinstance(v, dict):
            v = print_dict(v)
        if v is 'AAA':
            d[k] = 'XXX'
    return

DATA2 = print_dict(DATA)

print DATA