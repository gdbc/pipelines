#!/usr/bin/python
import rq
import prometheus_client
from rq.job import Job
from rq import registry
from redis import StrictRedis
from prometheus_client import Counter, Histogram


REQUEST_LATENCY = Histogram('finished_request_latency_seconds', 'Finished Request Latency', ['app_name', 'endpoint'], buckets=range(1,60))

REDIS_HOST = '172.17.0.1'
REDIS_PORT = '6379'

CON  = StrictRedis(host=REDIS_HOST, port=REDIS_PORT)


def mets():
   REG  = registry.FinishedJobRegistry('default', connection=CON)
   JOBS = REG.get_job_ids()

   for job_num in JOBS:
   
      job = Job.fetch(job_num, connection=CON)
      start    = job.started_at
      finish   = job.ended_at
      duration = finish - start
      #print "job number: ", job_num
      #print "job function name: ", job.func_name
      #print "job duration: ", duration.
      #print "job status: ", job.status
      #print "job result: ", job.result
      REQUEST_LATENCY.labels('web_api', job.func_name).observe(duration.total_seconds())
   return REQUEST_LATENCY
