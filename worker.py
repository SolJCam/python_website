import os
# from redis import Redis
import redis
from rq import Worker, Queue, Connection

'''
For local -
Make sure redis is installed: brew install redis; pip install rq
start redis server: redis-server
start worker: python worker.py or rq worker msnbc cnn fox   - if no name options are passed as arguments, will listen to default, resulting in this worker not receiving any jobs.
start dashboard: rq-dashboard
'''

# queue names to listen to. 
listen = ['msnbc', 'cnn', 'fox']

# return 'redis connection url' from environment variable and setting default value in the event key does not exist
redis_url = os.getenv('REDIS_TLS_URL', 'redis://localhost:6379')

# Tell RQ what Redis connection to use
conn = redis.from_url(redis_url)
# conn = Redis('localhost', 6379)   # for local use; also comment out redis_url variable and uncomment 'from redis import Redis'. Maybe unnecessary

if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(map(Queue, listen))
        worker.work()


