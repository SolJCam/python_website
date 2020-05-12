import os
# from redis import Redis
import redis
from rq import Worker, Queue, Connection

'''
For local:
start worker - python worker.py or rq worker
start redis server - 'redis-server /etc/redis/6379.conf'
start dashboard - rq-dashboard
'''

# queue names to listen to. 
listen = ['high', 'default', 'low']

# return 'redis connection url' from environment variable and setting default value in the event key does not exist
redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')

# Tell RQ what Redis connection to use
conn = redis.from_url(redis_url)
# conn = Redis('localhost', 6379)   # for local use; also comment out redis_url variable and uncomment 'from redis import Redis'. Maybe unnecessary

if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(map(Queue, listen))
        worker.work()


