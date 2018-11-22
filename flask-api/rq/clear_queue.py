#!/usr/bin/python
import rq
from rq import Queue
from rq.job import Job
from rq import registry
from redis import StrictRedis

REDIS_HOST = '172.17.0.1'
REDIS_PORT = '6379'

q
