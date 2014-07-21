'''
Created on Sep 18, 2013

@author: alex
'''
import time

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

def strip_expression(expression):
    stripped_expression = ""
    
    for line in expression.split('\n'):
        line = line.strip()
        if not line.startswith("#"):
            stripped_expression += line + ' '
            
    return stripped_expression.strip()

event_logs = [{
    "user_name" : "jim",
    "event_level" : "info",
    "package" : {"package_id" : "package1"},
    "message" : "system started"
}, {
    "user_name":"jim",
    "event_level":"error",
    "package" : {"package_id" : "package1"},
    "message" : "disk is full"
}, {
    "user_name":"alex",
    "event_level":"info",
    "package" : {"package_id" : "package1"},
    "message" : "delete share link"
}, {
    "user_name":"alex",
    "event_level":"error",
    "package" : {"package_id" : "package2"},
    "message" : "check password error"
}, {
    "user_name":"alex",
    "event_level":"notice",
    "package" : {"package_id" : "package3"},
    "message" : "share a file to friends",
    "to_users" : ["jim"]
}, {
    "user_name":"alex",
    "event_level":"notice",
    "package" : {"package_id" : "xx1"},
    "message" : "upload a file",
    "file_size" : "2g"
}, {
    "user_name":"alex123",
    "event_level":5,
    "package" : {"package_id" : "xx1"},
    "message" : "test operator event",
    "file_size" : "2g"
}]

pairs = [{
    "reg_id" : "reg1",
    "user_name" : "jim",
    "event_levels" : ["warn", "error"],
    "package_types" : ["package1", "package3"]
}, {
    "reg_id" : "reg2",
    "user_name" : "alex",
    "event_levels" : ["error"],
    "package_types" : ["package1", "package2"]
}, {
    "reg_id" : "reg3",
    "user_name" : "admin",
    "event_levels" : ["warn", "error"]
}, {
    "reg_id" : "reg_id1",
    "mobile_device_id" : "md1",
    "event_levels" : 3,
    "event_level_operator" : '>',
    "user_name" : "test_operator_higher_than",
    "package_types" : ["xx1"]
}, {
    "reg_id" : "reg_id1",
    "mobile_device_id" : "md1",
    "event_levels" : 2,
    "event_level_operator" : '<',
    "user_name" : "test_operator_less_than",
    "package_types" : ["xx1"]
}]

routing_rule = """
(not pair.package_types or event_log.package.package_id in pair.package_types)
and
(
    #pair.user_name == 'admin'
    #or
    (
        #event_log.event_level in ['info', 'warn', 'error']
        #and
        event_log.event_level {event_level_operator} pair.event_levels
    )
    or
    (
        event_log.event_level == 'notice'
        and
        event_log.user_name != pair.user_name and pair.user_name in event_log.to_users
    )
)
"""

routing_rule = strip_expression(routing_rule)
# func = compile(routing_rule, '<string>', 'eval')

start_time = time.time()
for i in xrange(1, 2):
#     for event_log in event_logs:
#         event_log = _Struct(event_log)
#          
#         for pair in pairs:
#             pair = _Struct(pair)
#                 
#             if not pair.package_types or event_log.package.package_id in pair.package_types:
#                 if event_log.event_level in ['info', 'warn', 'error'] and event_log.event_level in pair.event_levels:
#                     print "'%s' sent to %s" % (event_log.get('message'), pair.get('user_name'))
#                 elif event_log.event_level == 'notice' and event_log.user_name != pair.user_name and pair.user_name in event_log.to_users:
#                     print "'%s' sent to %s" % (event_log.get('message'), pair.get('user_name'))
#                 elif pair.user_name == 'admin':
#                     print "'%s' sent to %s" % (event_log.get('message'), pair.get('user_name'))
                     
    for event_log in event_logs:
        args = _Struct({"event_log" : event_log.copy()})
          
        for pair in pairs:
            args.update(_Struct({"pair" : pair}))
                     
            if not pair.get('event_level_operator'):
                pair['event_level_operator'] = 'in'
            routing_rule_formatted = routing_rule.format(event_level_operator=pair['event_level_operator'])
            print "routing_rule_formatted: ", routing_rule_formatted
            result = eval(routing_rule_formatted, args)
#             result = eval(func, args)
                     
            if result:
                print "'%s' sent to %s" % (event_log.get('message'), pair.get('user_name'))
                
print
print "spent %f seconds" % (time.time() - start_time)