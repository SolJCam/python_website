from apscheduler.schedulers.background import BackgroundScheduler
# from .rq_execution_schedule import execute_git_api
from rq_execution_schedule import execute_git_api
from datetime import datetime, date, timedelta, timezone
import pdb

UTCoffset = timedelta(hours=-4)
ESTtimezone = timezone(UTCoffset)

sched = BackgroundScheduler()

@sched.scheduled_job('interval', start_date=f'{date.today().isoformat()}T00:00:00Z', minutes=2)
# @sched.scheduled_job('interval', start_date=f'{date.today().isoformat()}T00:00:00Z', hours=8)
def schedule_api_call():
  print('initializing api call...')
  api_response = execute_git_api()
  print(f'api call complete at {datetime.now(ESTtimezone).strftime("%X%p")}')
  return api_response

sched.start()