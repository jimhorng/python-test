'''
Created on Apr 3, 2014

@author: jimhorng
'''

import operator

class _Struct(dict):
    def __init__(self, dict_, schema = None):
        if schema:
            super(_Struct, self).__init__(dict_)
        else :
            super(_Struct, self).__init__(dict_)
            
        for key in self:
            item = self[key]
            if isinstance(item, list):
                for idx, it in enumerate(item):
                    if isinstance(it, dict):
                        item[idx] = _Struct(it)
            elif isinstance(item, dict):
                self[key] = _Struct(item)

    def __getattr__(self, name):
        if self.has_key(name):
            return self[name]
        else:
            return {}
         
    def __setattr__(self, name, value):
        self[name] = value


EVENT_LEVEL = {
    "A" : "a",
    "B" : "b"
}

EVENT_LEVEL_CODE = {
    "a" : 2,
    "b" : 1,
    "c" : 0
}


a={'a':0, 'operator':operator}
expression = """
operator.gt(a,-1)
"""

expr1 = """
3 > 2 and 2 > 3
"""

expr2 = "EVENT_LEVEL_CODE.get(EVENT_LEVEL.A)"
expr3 = "EVENT_LEVEL.A"
expr4 = "EVENT_LEVEL_CODE.EVENT_LEVEL.A"

args = _Struct({"EVENT_LEVEL" : EVENT_LEVEL,
                "EVENT_LEVEL_CODE" : EVENT_LEVEL_CODE})
# args.update(_Struct({}))

print eval(expr3, args)
print eval(expr2, args)

# print "aa {haha}".format(haha="test123")
# 
# print eval(expression, a)
# 
# print "expr1", eval(expr1)
# 
# exec expression

if __name__ == "__main__":
    pass