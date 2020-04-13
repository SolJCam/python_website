import os, pdb
from rq.job import Job
from py_scraper.worker import hq_conn
from python_portfolio_site.local_settings import lcl_conn
from rq import Queue


try:
    if os.environ["SOLS_MAC"]:
        redis_q = Queue('default',connection=lcl_conn)
        redis_conn = lcl_conn

except Exception as e:
    redis_q = Queue('default',connection=hq_conn)
    redis_conn = hq_conn



def q_scrape(func, job_id):
    job = ""
    if job_id not in redis_q.job_ids:
        redis_q.enqueue(func, job_id=job_id, args=('request',))
        print('\n')
        print(redis_q.fetch_job(job_id))
        job = Job.fetch(job_id, connection=redis_conn)
        print(job.get_status()+'\n')
        # pdb.set_trace()
    
    redis_q.empty()

    return redis_q.fetch_job(job_id), job