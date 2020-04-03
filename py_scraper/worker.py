import os

import redis
from rq import Worker, Queue, Connection

# queue names to listen to. 
listen = ['high', 'default', 'low']

# return 'redis connection url' from environment variable and setting default value in the event key does not exist
redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')

# Tell RQ what Redis connection to use
conn = redis.from_url(redis_url)

if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(map(Queue, listen))
        worker.work()