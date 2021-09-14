from apscheduler.schedulers.background import BackgroundScheduler
from .rq_execution_schedule import execute_git_api
from datetime import datetime
import pdb

sched = BackgroundScheduler()

# @sched.scheduled_job('interval', start_date='2021-09-01', minutes=2)
@sched.scheduled_job('interval', start_date='2021-09-01', hours=8)
def schedule_api_call():
  print('initializing api call...')
  api_response = execute_git_api()
  print(f'api call complete at {datetime.now().strftime("%X%p")}')
  return api_response

sched.start()