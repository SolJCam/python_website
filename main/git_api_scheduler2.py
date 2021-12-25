# from .rq_execution_schedule import execute_git_api          # LOCAL USE
from rq_execution_schedule import execute_git_api             # REMOTE USE
from datetime import datetime, date, timedelta, timezone
import pdb

UTCoffset = timedelta(hours=-5)
ESTtimezone = timezone(UTCoffset)

def schedule_api_call():
  print('initializing api call...')
  execute_git_api()
  print(f'api call complete at {datetime.now(ESTtimezone).strftime("%X%p")}')
  return "success"

schedule_api_call()
