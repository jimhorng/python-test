'''
Created on Feb 14, 2014

@author: jimhorng
'''

from celery import Celery
# from kombu import Queue
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)
# app = Celery('celery_test', broker='pyamqp://192.168.69.2:5673')
app = Celery('celery_test', broker='amqp://192.168.69.1:5672')
# app = Celery('celery_test', broker='redis://192.168.68.234:6379/15')

EXCHANGE_NAME = 'celery_worker_test_exchange1'
QUEUE_NAME = "celery_worker_test_queue1"

app.conf.update(
    CELERY_INCLUDE = ['celery_worker_test'],
    CELERY_DEFAULT_EXCHANGE = EXCHANGE_NAME,
    CELERY_DEFAULT_QUEUE = QUEUE_NAME,
#     CELERY_QUEUES = (
#             Queue('celery_worker_test_queue',
#                   routing_key='celery_worker_test_key'),
#         ),
    CELERYD_HIJACK_ROOT_LOGGER = False,
#     CELERYD_CONCURRENCY = 4,
    CELERY_TASK_SERIALIZER = 'json',
    CELERY_ACCEPT_CONTENT = ['pickle', 'json', 'msgpack', 'yaml'],
    CELERYD_LOG_LEVEL = 'INFO',
#     CELERY_ROUTES = {
#         'celery_worker_test.test_task1': {
#             'queue': 'celery_worker_test_queue',
#             'routing_key': 'celery_worker_test_key'
#         }
#     }
)

def main():
#     app.worker_main()
    app.start()

@app.task
def test_task1(x, y):
    print "test_task1..." + str(x + y)

@app.task
def test_task2(x, y):
    print "test_task2..." + str(x * y)

@app.task
def test_task3(msg):
    logger.info("task completed")

if __name__ == '__main__':
    main()
