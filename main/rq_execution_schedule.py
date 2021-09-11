from rq import Queue
from worker import conn
from .git_api import git_api
import pdb

# redis_conn = conn
def execute_git_api():
  q = Queue(connection=conn)
  result = q.enqueue(git_api())
  return result

