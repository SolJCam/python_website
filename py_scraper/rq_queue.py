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

    print('\n')
    print(f'At start of current q...')
    print('\n')
    print(f'msnbc has:\n{len(FinishedJobRegistry(queue=msnbc_q))} jobs in FinishedJobRegistry and')
    print(f'{len(FailedJobRegistry(queue=msnbc_q))} jobs in FailedJobRegistry')
    print(f'cnn has:\n{len(FinishedJobRegistry(queue=cnn_q))} jobs in FinishedJobRegistry and')
    print(f'{len(FailedJobRegistry(queue=cnn_q))} jobs in FailedJobRegistry')
    print(f'fox has:\n{len(FinishedJobRegistry(queue=fox_q))} jobs in FinishedJobRegistry and')
    print(f'{len(FailedJobRegistry(queue=fox_q))} jobs in FailedJobRegistry\n')
    
    # pdb.set_trace()
    if job_id == "msnbc" and job_id not in msnbc_q.job_ids:
        # pdb.set_trace()
        msnbc_q.enqueue(func, job_id=job_id, default_timeout=600, failure_ttl=300, args=(func_args[0],func_args[1],func_args[2]))
        msnbc_job = Job.fetch(job_id, connection=redis_conn)
        status = msnbc_job.get_status()
        print('\n')
        # print(msnbc_job)
        # print(msnbc_q.count)
        # print(status+'\n')
        print(f'{status, msnbc_job} on msnbc_q\n')
        if msnbc_q.count > 20:
            msnbc_q.empty()
            print(f'Emptied msnbc_q job queue\n')

    if job_id == "cnn" and job_id not in cnn_q.job_ids:
        # pdb.set_trace()
        cnn_q.enqueue(func, job_id=job_id, default_timeout=600, failure_ttl=300, args=(func_args[0],func_args[1],func_args[2]))
        cnn_job = Job.fetch(job_id, connection=redis_conn)
        status = cnn_job.get_status()
        print('\n')
        print(f'{status, cnn_job} on cnn_q\n')
        if cnn_q.count > 20:
            cnn_q.empty()
            print(f'Emptied cnn_q job queue\n')

    if job_id == "fox" and job_id not in fox_q.job_ids:
        # pdb.set_trace()
        fox_q.enqueue(func, job_id=job_id, default_timeout=600, failure_ttl=300, args=(func_args[0],func_args[1],func_args[2]))
        fox_job = Job.fetch(job_id, connection=redis_conn)
        status = fox_job.get_status()
        print('\n')
        print(f'{status, fox_job} on fox_q\n')
        if fox_q.count > 20:
            fox_q.empty()
            print(f'Emptied fox_q job queue\n')

    # pdb.set_trace()

    workers = Worker.all(connection=conn)

    print(f'Worker is {workers[0].state}')
    try:
        print(f'Current job is {workers[0].current_job}')
    except:
        print(f'Currently no jobs executing on worker')
    print('\n')


    '''Allows for jobs to complete'''
    # time.sleep(210)       

    
    '''
    Only useful is sleep function above is used. 
    Otherwise total sum of jobs in both regstries will not account for the current, incomplete jobs
    '''
    # if job_id =='msnbc' and 'msnbc' in FinishedJobRegistry(queue=msnbc_q):
    #     print('msnbc is in FinishedJobRegistry')
    #     FinishedJobRegistry(queue=msnbc_q).remove(job_id)
    # elif job_id =='msnbc' and 'msnbc' in FailedJobRegistry(queue=msnbc_q):
    #     print('msnbc is in FailedJobRegistry')
    #     FailedJobRegistry(queue=msnbc_q).remove(job_id)

    # if job_id =='cnn' and 'cnn' in FinishedJobRegistry(queue=cnn_q):
    #     print('cnn is in FinishedJobRegistry')
    #     FinishedJobRegistry(queue=cnn_q).remove(job_id)
    # elif job_id =='cnn' and 'cnn' in FailedJobRegistry(queue=cnn_q):
    #     print('cnn is in FailedJobRegistry')
    #     FailedJobRegistry(queue=cnn_q).remove(job_id)

    # if job_id =='fox' and 'fox' in FinishedJobRegistry(queue=fox_q):
    #     print('fox is in FinishedJobRegistry')
    #     FinishedJobRegistry(queue=fox_q).remove(job_id)
    # elif job_id =='fox' and 'fox' in FailedJobRegistry(queue=fox_q):
    #     print('fox is in FailedJobRegistry')
    #     FailedJobRegistry(queue=fox_q).remove(job_id)

    if len(FinishedJobRegistry(queue=msnbc_q)) > 20:
        FinishedJobRegistry(queue=msnbc_q).remove('msnbc')
        print(f'FinishedJobRegistry for msnbc_q reset to: {len(FinishedJobRegistry(queue=msnbc_q))}')
    if len(FinishedJobRegistry(queue=cnn_q)) > 20:
        FinishedJobRegistry(queue=cnn_q).remove('cnn')
        print(f'FinishedJobRegistry for cnn_q reset to: {len(FinishedJobRegistry(queue=cnn_q))}')
    if len(FinishedJobRegistry(queue=fox_q)) > 20:
        FinishedJobRegistry(queue=fox_q).remove('fox')
        print(f'FinishedJobRegistry for fox_q reset to: {len(FinishedJobRegistry(queue=fox_q))}')

    if len(FailedJobRegistry(queue=msnbc_q)) > 20:
        FailedJobRegistry(queue=msnbc_q).remove('msnbc')
        print(f'FailedJobRegistry for msnbc_q reset to: {len(FailedJobRegistry(queue=msnbc_q))}')
    if len(FailedJobRegistry(queue=cnn_q)) > 20:
        FailedJobRegistry(queue=cnn_q).remove('cnn')
        print(f'FailedJobRegistry for cnn_q reset to: {len(FailedJobRegistry(queue=cnn_q))}')
    if len(FailedJobRegistry(queue=fox_q)) > 20:
        FailedJobRegistry(queue=fox_q).remove('fox')
        print(f'FailedJobRegistry for fox_q reset to: {len(FailedJobRegistry(queue=fox_q))}')

    print(f'Jobs by queue: \nmsnbc - {msnbc_q.count}\ncnn - {cnn_q.count}\nfox - {fox_q.count}\ntotal - {msnbc_q.count+cnn_q.count+fox_q.count}')
    print(f'Total jobs successfully completed on worker: {workers[0].successful_job_count}')
    print(f'Total jobs failed to complete on worker: {workers[0].failed_job_count}')
    print('\n')

    return 'success'