caches = {}
kwd_mark = object

def cache_result(func):
    def wrapper(*args, **kwargs):
        global caches
        key = args + (kwd_mark,) + tuple(sorted(kwargs.items()))
        if caches.get(key):
            return caches.get(key)
        else:
            result = func(*args, **kwargs)
            caches[key] = result
            return result
    return wrapper
    
# Unit test
count = 0

@cache_result
def f1(k):
    global count
    count +=1
    return k

f1(1)
assert count == 1
f1(1)
assert count == 1
f1(2)
assert count == 2
f1(3)
assert count == 3
f1(2)
assert count == 3
print 'passed'

# Another unit test
count2 = 0

@cache_result
def f2(x, y, z=10):
    global count2
    count2 +=1
    return (x, y)
f2('a', 'b')
assert count2 == 1
f2('a', 'b')
assert count2 == 1
f2('a', 'b', z=11)
assert count2 == 2
f2('a', 'b', z=11)
assert count2 == 2
f2('b', 'a', z=12)
assert count2 == 3
print 'passed'