import time

class TimeBoundedDict(dict):
    def __init__(self, countdown):
        super(TimeBoundedDict, self).__init__()
        self.countdown = countdown
        self.timer = {}

    def __setitem__(self, key, val):
        self.timer[key] = time.time()
        super(TimeBoundedDict, self).__setitem__(key, val)
    
    def __getitem__(self, key):
        if super(TimeBoundedDict, self).__getitem__(key) and (time.time() - self.timer[key]) >= self.countdown:
            super(TimeBoundedDict, self).__setitem__(key, None)
        return super(TimeBoundedDict, self).__getitem__(key)

# Unit test
import time

d = TimeBoundedDict(1)
d['a'] = 'abc'
assert d['a'] == 'abc'
time.sleep(2)
assert d['a'] == None
print 'passed'