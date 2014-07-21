# -*- coding: utf-8 -*-

import json

def unicode_truncate(s, length, encoding='utf-8', postfix="..."):
    length = length - len(postfix)
    if length < 0: length = 0
    encoded = s.encode(encoding)[:length]
    return encoded.decode(encoding, 'ignore') + postfix

def string_type(s):
    if isinstance(s, str):
        return "ordinary string"
    elif isinstance(s, unicode):
        return "unicode string"
    else:
        return "not a string"

def dict_json_length(the_dict):
    return len(json.dumps(the_dict, separators=(',',':'), ensure_ascii=False).encode('utf-8'))

MAX_LENGTH = 49
unicode_str =  unicode('這是中文', 'utf-8')

json_dict = {
                'message' : u"這是中文這是中文這是中文這是中文這是中文",
                'b' : "test",
                'c' : "哈哈"
             }



a_str = json.dumps(json_dict)
b_str = json.dumps(json_dict, separators=(',',':'), ensure_ascii=False).encode('utf-8')
json_dict_new = json_dict.copy()
print "org len: ", dict_json_length(json_dict_new)
json_dict_new['message'] = ""
non_changable_length = dict_json_length(json_dict_new)
print "non-changable len: ", non_changable_length
message_max_length = MAX_LENGTH - non_changable_length
if message_max_length < 0: message_max_length = 0
json_dict_new['message'] = unicode_truncate(json_dict['message'], message_max_length)
print "truncated len: ", dict_json_length(json_dict_new)
print "truncated raw: ", json.dumps(json_dict_new, separators=(',',':'), ensure_ascii=False).encode('utf-8')

t2_org = u"這是中文123一二三"
t_len = 10
t2 = unicode_truncate(t2_org, t_len)
print "t2_org: " , t2_org, " len: ", len(t2_org), "\ttype: ", string_type(t2_org)
print "t2: " , t2, " t_len: ", t_len, "\ttype: ", string_type(t2)
print "t2 len: ", len(t2)
print "t2 encode('utf-8'): ", t2.encode('utf-8'), "\ttype: ", string_type(t2.encode('utf-8'))
print "t2 len utf8: ", len(t2.encode('utf-8'))

t3 = unicode_truncate("12345", 4)
print "t3: ", t3
print "t3 len: ", len(t3)

print "b_str: ", b_str
print "b_str len: ", len(b_str)
print "b_str trun: ", unicode_truncate(b_str, 10)