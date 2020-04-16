# import os, pdb
# from rq.job import Job
# from py_scraper.worker import hq_conn
# # from python_portfolio_site.local_settings import lcl_conn
# from rq import Queue
# # from rq.registry import StartedJobRegistry, FinishedJobRegistry, FailedJobRegistry, DeferredJobRegistry, 
# # import time


# try:
#     if os.environ["SOLS_MAC"]:
#         redis_q = Queue('default',connection=lcl_conn)
#         redis_conn = lcl_conn

# except Exception as e:
#     redis_q = Queue('default',connection=hq_conn)
#     redis_conn = hq_conn



# def q_scrape(func, job_id):
#     job = "" 

#     # job = redis_q.enqueue(func, job_id=job_id, args=('request',))

#     # registry = StartedJobRegistry(queue=redis_q)
#     # time.sleep(0.1)
#     # print(registry.get_queue())
#     # print(registry.count)
#     # print(registry.get_job_ids())
#     # print((job in registry))
#     # print((job.id in registry))
#     # print(redis_q.started_job_registry)  
#     # print(redis_q.deferred_job_registry)   
#     # print(redis_q.finished_job_registry)  
#     # print(redis_q.failed_job_registry)  
#     # print(redis_q.scheduled_job_registry)

#     # pdb.set_trace()
#     ok = ""
#     if job_id not in redis_q.job_ids:
#         # pdb.set_trace()
#         ok = redis_q.enqueue(func, job_id=job_id, args=('request',))
#         # redis_q.enqueue(func, job_id=job_id, args=('request',))
#         print('\n')
#         # print(redis_q.fetch_job(job_id))
#         job = Job.fetch(job_id, connection=redis_conn)
#         print(job)
#         print(job.get_status()+'\n')

#         # pdb.set_trace()
    
#     print(ok)

#     redis_q.empty()

#     return job