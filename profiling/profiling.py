'''
Created on Jun 4, 2014

@author: jimhorng
'''
import yappi
import apns_test
import signal
import sys

def sys_exit_call(signum, frame):
    print "profiling result:"
    yappi.get_func_stats().print_all(columns={0:("name",100), 1:("ncall", 15), 
                    2:("tsub", 8), 3:("ttot", 8), 4:("tavg",8)})
    yappi.get_thread_stats().print_all()
    sys.exit(1)

yappi.start()

# import atexit
# atexit.register(sys_exit_call)
signal.signal(signal.SIGUSR2, sys_exit_call)

apns_test.main()
import time
time.sleep(1000)