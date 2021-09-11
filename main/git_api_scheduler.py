from apscheduler.schedulers.blocking import BlockingScheduler
from .rq_execution_schedule import execute_git_api
from .git_api import git_api
import pdb

sched = BlockingScheduler()

# @sched.scheduled_job('interval', hour=8)
@sched.scheduled_job('interval', minutes=2)
def schedule_api_call():
  print('initializing api call...')
#   api_response = git_api()
  api_response = execute_git_api()
#   pdb.set_trace()
  print('api call complete')
  return api_response

sched.start()