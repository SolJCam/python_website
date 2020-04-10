from rq import Queue
from py_scraper.worker import conn
from py_scraper.views import scrape_msnbc, scrape_cnn, scrape_fox
import pdb

# no args implies the default queue
q = Queue('default',connection=conn)

msnbc_result = q.enqueue(scrape_msnbc, job_id='msnbc', args=('request',))
cnn_result = q.enqueue(scrape_cnn, job_id='cnn', args=('request',))
fox_result = q.enqueue(scrape_fox, job_id='fox', args=('request',))
# msnbc_result = q.enqueue(scrape_msnbc)
# cnn_result = q.enqueue(scrape_cnn)
# fox_result = q.enqueue(scrape_fox)

pdb.set_trace()
# Examples of how to retrieve jobs
# queued_jobs = q.jobs # Gets a list of enqueued job instances
# queued_job_ids = q.job_ids # Gets a list of job IDs from the queue
# job = q.fetch_job('my_id') # Returns job having ID "my_id"

# Printing jobs based on IDs
queued_job_ids = q.job_ids
for job_id in queued_job_ids:
    print(q.fetch_job(job_id))

# Emptying a queue, this will delete all jobs in this queue
q.empty()