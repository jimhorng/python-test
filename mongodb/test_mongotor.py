from tornado.testing import gen_test
from tornado.ioloop import IOLoop
from functools import partial

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
    delete_tests(None)
#     IOLoop.instance().run_sync(get_instance().test123.remove)

@gen_test
def delete_tests(self):
    get_instance().test123.remove()

if __name__ == '__main__':
    main()
