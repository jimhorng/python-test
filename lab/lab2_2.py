def fibonacci():
    i1 = 0
    i2 = 1
    yield i1
    yield i2
    while True:
        i3 = i1 + i2
        i1 = i2
        i2 = i3
        yield i3

# Unit test
import itertools

for n in itertools.islice(fibonacci(), 13):
    print n
assert list(itertools.islice(fibonacci(), 13)) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
print 'passed'