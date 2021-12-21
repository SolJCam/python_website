from rq import Queue
# from worker import conn           # LOCAL USE
# from .git_api import git_api      # LOCAL USE
# from redis import Redis           # LOCAL USE
from git_api import git_api         # REMOTE USE
import os                           # REMOTE USE

# conn = Redis('localhost', 6379)                                   # LOCAL USE
conn = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')         # REMOTE USE

q = Queue(connection=conn)
def execute_git_api():
  result = q.enqueue(git_api)
  return result

