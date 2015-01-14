'''
Created on Jan 13, 2015

@author: jimhorng
'''
def is_string_symmetric(the_string):
    for i in xrange(len(the_string) / 2 ):
        if the_string[i] != the_string[-1-i]:
            return False
    return True

if __name__ == "__main__":
    print is_string_symmetric("apple")
    print is_string_symmetric("abcdcba")
    print is_string_symmetric("abccba")