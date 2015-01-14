'''
Created on Feb 25, 2014

@author: jimhorng
'''
from fabric.api import run, cd, env, put, parallel, execute, task, runs_once
from fabric.contrib.files import exists
from os import path
from fabric.context_managers import shell_env
import json

import mq_consume_timer

env.hosts = [
    'jimhorng@127.0.0.1',
    'root@qcloud-dev-mq2',
    'root@qcloud-dev-mq3',
#     'root@qcloud-dev-mq1'
]

WORKERS_PER_HOST = 2
MSG_PER_SENDER = int(0.01 * 10000)
SENDER_PER_HOST = 2
TOTAL_MSG = MSG_PER_SENDER * SENDER_PER_HOST * len(env.hosts)

script_original_dir = '/Users/jimhorng/workspace/py_test/celery_test'
script_remote_dir = '/tmp/celery_test'
remote_venv_dir = '/tmp/venv-test'
remote_venv_bin_dir = path.join(remote_venv_dir, 'bin')
python_bin_path = path.join(remote_venv_bin_dir, 'python')
celery_bin_path = path.join(remote_venv_bin_dir, 'celery')
pip_bin_path = path.join(remote_venv_bin_dir, 'pip')

is_inited = False

@task
@parallel
def sender_test():
    with cd(script_remote_dir):
        result = run(python_bin_path + ' celery_sender_test.py --msg-qty=' + str(MSG_PER_SENDER) +
                     ' --sender-qty=' + str(SENDER_PER_HOST))
    return result

@task
@parallel
def init():
    run('mkdir -p ' + script_remote_dir)
    put(path.join(script_original_dir,'*.py'), script_remote_dir)
    if not exists(celery_bin_path):
        run('virtualenv ' + remote_venv_dir)
        run(pip_bin_path + ' install celery')

@task
@parallel
def worker_start():
    with shell_env(C_FORCE_ROOT='true'):
        with cd(script_remote_dir):
            run(celery_bin_path + ' multi start ' + 
                    str(WORKERS_PER_HOST) + 
                    ' --app=celery_worker_test --loglevel=error',
                pty=False)

@task
@parallel
def worker_stop():
    with cd(script_remote_dir):
        run(celery_bin_path + ' multi stop ' + 
                str(WORKERS_PER_HOST),
            pty=False)
        run(celery_bin_path + ' multi kill ' + 
                str(WORKERS_PER_HOST),
            pty=False)

@task
@runs_once
def sender():
    execute(init)
    results = execute(sender_test)
    print "result: ", combine_result(results)

@task
@runs_once
def worker():
    execute(init)
    MSG_QTY = mq_consume_timer.get_message_qty_from_default_queue()
    print "msg before: ", MSG_QTY
    execute(worker_start)
    time = mq_consume_timer.wait_and_get_msg_consuming_time()
    execute(worker_stop)
    print json.dumps({'worker_total_rate' : int(TOTAL_MSG / time),
                      'msg_delta_rate' : int(MSG_QTY / time),
                      'msg_delta' : MSG_QTY,
                      'time_elapsed' : time})

def combine_result(results):
    combined_result = {}
    combined_result['rate_total'] = 0
    combined_result['sent_total'] = 0
    for _, result in results.items():
        combined_result['rate_total'] += int(json.loads(result)['rate'])
        combined_result['sent_total'] += int(json.loads(result)['sent'])
    return combined_result

if __name__ == '__main__':
    pass