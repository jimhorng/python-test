'''
Created on Mar 4, 2014

@author: jimhorng
'''

import kombu

def main():
#     conn = kombu.Connection("pyamqp://qcloud-dev-mq1:5672//")
    conn = kombu.Connection("amqp://qcloud-dev-mq1:5672//")
    amqp_channel = conn.channel()
    kombu.Exchange(name='test123123123', channel=amqp_channel).delete()
    kombu.Queue(name='qcloud.celery.unittest4636', channel=amqp_channel).delete()
    # real_exchange = news_exchange(amqp_channel)
    # real_exchange.declare()
    # outgoing.exchange_delete("test123")

if __name__ == '__main__':
    main()