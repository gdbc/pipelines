#!/usr/bin/python
import rq
import prometheus_client
from rq.job import Job
from rq import registry
from redis import StrictRedis
from prometheus_client import Counter, Histogram, Summary


CHECKSVC_LATENCY = Histogram('histogram_check_svc_latency_seconds', 'Histogram Service Check Latency', ['app_name', 'endpoint'],buckets=[ round(x * 0.1, 1) for x in range(0, 10)])

BUILDVM_LATENCY = Histogram('histogram_buildvm_latency_seconds', 'Histogram Buildvm Check Latency', ['app_name', 'endpoint'],buckets=range(100, 200,10))


REDIS_HOST = '172.17.0.1'
REDIS_PORT = '6379'
CON        = StrictRedis(host=REDIS_HOST, port=REDIS_PORT)

def mets(queue_name):
   REG  = registry.FinishedJobRegistry(queue_name, connection=CON)
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
      if job.func_name.split(".")[1] == "check_svc":
        CHECKSVC_LATENCY.labels('/cs', job.func_name).observe(duration.total_seconds())
      elif job.func_name.split(".")[1] == "build_system":
        BUILDVM_LATENCY.labels('/cs', job.func_name).observe(duration.total_seconds())
      #REQUEST_SUMMARY.labels('/cs', job.func_name).observe(duration.total_seconds())
 
   rm_queue(queue_name)
   #return REQUEST_LATENCY, REQUEST_SUMMARY
   return CHECKSVC_LATENCY, BUILDVM_LATENCY

def rm_queue(queue_name):
   REG  = registry.FinishedJobRegistry(queue_name, connection=CON)

   if REG.count > 0:
      JOBS = REG.get_job_ids()
      for job_num in JOBS:
         job = Job.fetch(job_num, connection=CON)
         job.delete()
