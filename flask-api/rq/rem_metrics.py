#!/usr/bin/python
import rq
from rq.job import Job
from rq import registry
from redis import StrictRedis

REDIS_HOST = '172.17.0.1'
REDIS_PORT = '6379'

CON  = StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
REG  = registry.FinishedJobRegistry('default', connection=CON)

if REG.count > 0:
   JOBS = REG.get_job_ids()
   for job_num in JOBS:
      job = Job.fetch(job_num, connection=CON)
      job.delete()
      print "Job Count: ", REG.count
