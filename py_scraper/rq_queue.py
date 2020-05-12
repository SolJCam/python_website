import os, pdb
from rq.job import Job
from worker import conn
from rq import Queue
# from rq.registry import StartedJobRegistry, FinishedJobRegistry, FailedJobRegistry, DeferredJobRegistry 
import time

redis_q = Queue('default',connection=conn)
redis_conn = conn

def q_scrape(func, job_id):
    
    start = time.time()
    job = "" 

    # pdb.set_trace()
    ok = ""
    if job_id not in redis_q.job_ids:
        # pdb.set_trace()
        ok = redis_q.enqueue(func, job_id=job_id, args=('request',))
        job = Job.fetch(job_id, connection=redis_conn)
        print('\n')
        print(job)
        print(job.get_status()+'\n')

        # pdb.set_trace()
    
    end = time.time()
    time_elapsed = end - start
    print(time_elapsed)
    
    # pdb.set_trace()

    redis_q.empty()
    
    return func('request'), job