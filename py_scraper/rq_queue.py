import requests, pdb
from rq import Queue
from py_scraper.worker import conn
from py_scraper.views import scrape_msnbc, scrape_cnn, scrape_fox

# no args implies the default queue
q = Queue(connection=conn)

msnbc_result = q.enqueue(scrape_msnbc, 'request', job_id='msnbc')
cnn_result = q.enqueue(scrape_cnn, 'request', job_id='cnn')
fox_result = q.enqueue(scrape_fox, 'request', job_id='fox')

# Getting the number of jobs in the queue
print(len(q))

pdb.set_trace()
# Examples of how to retrieve jobs
# queued_jobs = q.jobs # Gets a list of enqueued job instances
# queued_job_ids = q.job_ids # Gets a list of job IDs from the queue
# job = q.fetch_job('my_id') # Returns job having ID "my_id"

# Printing jobs based on IDs
queued_job_ids = q.job_ids
for job_id in queued_job_ids:
    print(q.fetch_job(job_id)