from rq import Queue
# from worker import conn
# from .git_api import git_api
import pdb
# from redis import Redis
from git_api import git_api
import os

# conn = Redis('localhost', 6379)
conn = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')
def execute_git_api():
  q = Queue(connection=conn)
  result = q.enqueue(git_api())
  return result

