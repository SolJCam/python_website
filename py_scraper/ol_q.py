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
        ok = redis_q.enqueue(func, job_id=job_id, default_timeout=600, args=('request',))
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





# def q_scrape(func, func_args, job_id):
    
#     start = time.time()
#     job = "" 
#     status = ""
#     # pdb.set_trace()
#     if job_id not in redis_q.job_ids:
#         # pdb.set_trace()
#         redis_q.enqueue(func, job_id=job_id, default_timeout=600, args=(func_args[0],func_args[1],func_args[2]))
#         job = Job.fetch(job_id, connection=redis_conn)
#         status = job.get_status()
#         print('\n')
#         print(job)
#         print(status+'\n')

#         # pdb.set_trace()
    
#     end = time.time()
#     time_elapsed = end - start
#     # print("Time elapsed to "+status+" "+job_id+" job: "+str(round(time_elapsed,2))+" secs")
    
#     # pdb.set_trace()

#     redis_q.empty()
    
#     return job