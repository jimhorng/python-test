from tornado.testing import gen_test
from tornado.ioloop import IOLoop
from tornado import gen
from tornado.gen import Return
from functools import partial
import timeit

import sys
import qnap.common.logutil as logutil
from qnap.common.jsonutil import json2dict
from qnap.common.jsonutil import dict2json
from qnap.common.mongoutil import get_instance

def main():
    print "sys.path: ", sys.path
    logutil.initialize()
    from qnap.common.logutil import get_logger
    _logger = get_logger(__name__)
    
    _logger.info("starting...")
    
    import qnap.common.configutil as configutil
    configutil.initialize("^env((?!amp|auth_center).)*\.conf$")
    
    import qnap.common.mongoutil as mongoutil
    mongoutil.initialize()
#     delete_tests(None)
    licenses_record = run_get_licenses()
#     licenses_record = run_get_licenses_n_queries()
    print licenses_record

#     print timeit.timeit(stmt="run_get_licenses()",
#                         setup="from __main__ import run_get_licenses",
#                         number=1000)
#     print timeit.timeit(stmt="run_get_licenses_n_queries()",
#                         setup="from __main__ import run_get_licenses_n_queries",
#                         number=1000)

@gen.coroutine
def get_licenses_n_queries():
    licenses, error = yield gen.Task(get_instance().license.find,
                              { 'user_id': "5253839f50f6457f7e47b7e6" } )

    for the_license in licenses:
        if the_license.get('applied_on_device_id'):
            device, error = yield gen.Task(get_instance().device.find_one,
                                           { '_id': the_license.get('applied_on_device_id') }
                                           )
            if device and device.get('info'):
                the_license['device_model_name'] = device.get('info').get('model_name')

    raise Return(licenses)

@gen.coroutine
def get_licenses():
    licenses, error = yield gen.Task(get_instance().license.find,
                              { 'user_id': "5253839f50f6457f7e47b7e6" } )

    device_ids = [ the_license['applied_on_device_id']
                  for the_license in licenses
                  if the_license.get('applied_on_device_id') ]

    devices, error = yield gen.Task(get_instance().device.find,
                                    { '_id': { '$in': device_ids } }
    )
    devices_dict = { device['_id'] : device for device in devices }

    def join_device(the_license, devices_dict):
        if the_license.get('applied_on_device_id'):
            the_license['device_model_name'] = None
            device = devices_dict.get(the_license.get('applied_on_device_id'))
            if device and device.get('info'):
                 the_license['device_model_name'] = device.get('info').get('model_name')
        return the_license
    licenses = [ join_device(the_license, devices_dict) for the_license in licenses ]
#     licenses = map(join_device, licenses)

#     for the_license in licenses:
#         if the_license.get('applied_on_device_id'):
#             device = devices_dict.get(the_license.get('applied_on_device_id'))
#             if device and device.get('info'):
#                 the_license['device_model_name'] = device.get('info').get('model_name')

    raise Return(licenses)

def run_get_licenses():
    licenses_record = IOLoop.instance().run_sync(get_licenses)
    return licenses_record

def run_get_licenses_n_queries():
    licenses_record = IOLoop.instance().run_sync(get_licenses_n_queries)
    return licenses_record

if __name__ == '__main__':
    main()
