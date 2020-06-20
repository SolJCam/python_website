import os, pdb
from rq.job import Job
from worker import conn
from rq import Queue, Worker, get_current_job
from rq.registry import StartedJobRegistry, FinishedJobRegistry, FailedJobRegistry, DeferredJobRegistry 
import time

redis_conn = conn

msnbc_q = Queue('msnbc',connection=conn)
cnn_q = Queue('cnn',connection=conn)
fox_q = Queue('fox',connection=conn)


def q_scrape(func, func_args, job_id):
    
    # pdb.set_trace()
    if job_id == "msnbc" and job_id not in msnbc_q.job_ids:
        # pdb.set_trace()
        msnbc_q.enqueue(func, job_id=job_id, default_timeout=600, failure_ttl=300, args=(func_args[0],func_args[1],func_args[2]))
        msnbc_job = Job.fetch(job_id, connection=redis_conn)
        status = msnbc_job.get_status()
        print('\n')
        print(msnbc_job)
        print(status+'\n')

    if job_id == "cnn" and job_id not in cnn_q.job_ids:
        # pdb.set_trace()
        cnn_q.enqueue(func, job_id=job_id, default_timeout=600, failure_ttl=300, args=(func_args[0],func_args[1],func_args[2]))
        cnn_job = Job.fetch(job_id, connection=redis_conn)
        status = cnn_job.get_status()
        print('\n')
        print(cnn_job)
        print(status+'\n')

    if job_id == "fox" and job_id not in fox_q.job_ids:
        # pdb.set_trace()
        fox_q.enqueue(func, job_id=job_id, default_timeout=600, failure_ttl=300, args=(func_args[0],func_args[1],func_args[2]))
        fox_job = Job.fetch(job_id, connection=redis_conn)
        status = fox_job.get_status()
        print('\n')
        print(fox_job)
        print(status+'\n')

    # pdb.set_trace()

    workers = Worker.all(connection=conn)

    print(workers[0].state)
    print(workers[0].queues)
    print('\n')


    # time.sleep(210)

    if job_id =='msnbc' and 'msnbc' in FinishedJobRegistry(queue=msnbc_q):
        print('msnbc is in FinishedJobRegistry')
        FinishedJobRegistry(queue=msnbc_q).remove(job_id)
    elif job_id =='msnbc' and 'msnbc' in FailedJobRegistry(queue=msnbc_q):
        print('msnbc is in FailedJobRegistry')
        FailedJobRegistry(queue=msnbc_q).remove(job_id)

    if job_id =='cnn' and 'cnn' in FinishedJobRegistry(queue=cnn_q):
        print('cnn is in FinishedJobRegistry')
        FinishedJobRegistry(queue=cnn_q).remove(job_id)
    elif job_id =='cnn' and 'cnn' in FailedJobRegistry(queue=cnn_q):
        print('cnn is in FailedJobRegistry')
        FailedJobRegistry(queue=cnn_q).remove(job_id)

    if job_id =='fox' and 'fox' in FinishedJobRegistry(queue=fox_q):
        print('fox is in FinishedJobRegistry')
        FinishedJobRegistry(queue=fox_q).remove(job_id)
    elif job_id =='fox' and 'fox' in FailedJobRegistry(queue=fox_q):
        print('fox is in FailedJobRegistry')
        FailedJobRegistry(queue=fox_q).remove(job_id)


    if workers[0].successful_job_count > 0:
        print('\n')
        print(f'There are {workers[0].successful_job_count} successfull jobs on the worker')
    if workers[0].failed_job_count > 0:
        print(f'There are {workers[0].failed_job_count} failed jobs on the worker \n')

    # redis_q.empty()
    
    return 'success'