'''
Created on Feb 19, 2014

@author: jimhorng
'''

from celery_sender_test import MSG_QTY

file_path = "./output/test_output1.log"

import re
pattern_received = r"\[(\d+-\d+-\d+ \d+:\d+:\d+,\d+): INFO/MainProcess\] Received task.+"
pattern_processed = r"\[(\d+-\d+-\d+ \d+:\d+:\d+,\d+): INFO/MainProcess\] Task.+succeeded"
pattern_logged = r"\[(\d+-\d+-\d+ \d+:\d+:\d+,\d+): INFO/Worker-\d+\].+task completed"

# time_stamps_received = []
# time_stamps_processed = []
time_stamps_logged = []

with open(file_path) as f:
    for line in f:
#         matches_received = re.match(pattern_received, line)
#         if matches_received:
#             time_stamps_received.append(matches_received.group(1))
#         matches_processed = re.match(pattern_processed, line)
#         if matches_processed:
#             time_stamps_processed.append(matches_processed.group(1))
        matches_logged = re.match(pattern_logged, line)
        if matches_logged:
            time_stamps_logged.append(matches_logged.group(1))


import datetime
# time_format = "YYYY-MM-DD HH:MM:SS,mmm"
time_format = "%Y-%m-%d %H:%M:%S,%f"
time_start = datetime.datetime.strptime(time_stamps_logged[0], time_format)
time_end = datetime.datetime.strptime(time_stamps_logged[-1], time_format)

time_elapsed = (time_end - time_start).total_seconds()
# msg_received = len(time_stamps_received)
# msg_processed = len(time_stamps_processed)
msg_logged = len(time_stamps_logged)
rate = int( msg_logged / time_elapsed )

print "time elapsed: ", time_elapsed

print "msg expected: ", MSG_QTY
# print "msg received: ", msg_received, "\t*rate: ", ( msg_received / time_elapsed ), "/s"
# print "msg_processed: ", msg_processed
print "msg_logged: ", msg_logged, "\t*rate: ", rate, "/s"

if __name__ == '__main__':
    pass