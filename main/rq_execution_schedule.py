from rq import Queue
# from worker import conn
# from redis import Redis
import os
from git_api import git_api
import pdb

# conn = Redis('localhost', 6379)
conn = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')
def execute_git_api():
  q = Queue(connection=conn)
  result = q.enqueue(git_api())
  return result

