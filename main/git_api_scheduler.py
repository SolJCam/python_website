from apscheduler.schedulers.background import BackgroundScheduler
# from .rq_execution_schedule import execute_git_api          # LOCAL USE
from rq_execution_schedule import execute_git_api             # REMOTE USE
from datetime import datetime, date, timedelta, timezone
import pdb

UTCoffset = timedelta(hours=-5)
ESTtimezone = timezone(UTCoffset)

sched = BackgroundScheduler()

@sched.scheduled_job('interval', start_date=f'{date.today().isoformat()}T00:00:00Z', minutes=2)
# @sched.scheduled_job('interval', start_date=f'{date.today().isoformat()}T00:00:00Z', hours=8)
def schedule_api_call():
  print('initializing api call...')
  execute_git_api()
  print(f'api call complete at {datetime.now(ESTtimezone).strftime("%X%p")}')
  return "success"

schedule_api_call()

sched.start()