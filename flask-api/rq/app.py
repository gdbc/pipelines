#!/usr/bin/python3.4
import prometheus_client
from flask import Flask, jsonify, request, Response
from redis import StrictRedis
from rq import Queue
from sums import add
from vmcreate import build_system
from checksvc import check_svc
from flask_prometheus import monitor 
from get_mets import mets

from random import randrange

REDIS_HOST="172.17.0.1"
REDIS_PORT="6379"

CONTENT_TYPE_LATEST = str('text/plain; version=0.0.4; charset=utf-8')


app = Flask(__name__)

q = Queue('default',connection=StrictRedis(host=REDIS_HOST, port=REDIS_PORT))

@app.route('/')
def get_randrange():
    one = request.args.get('one')
    two = request.args.get('two')
    #job = q.enqueue(randrange, start, stop, step, result_ttl=5000)
    job = q.enqueue(add, one, two)
    job_id = job.get_id()
    return job_id

@app.route("/checkservice")
def check_service():
    vm = request.args.get("vmname")
    sv    = request.args.get("svc")
    print("%s %s" %(vm,sv))
    job = q.enqueue(check_svc, vm, sv)
    job_id = job.get_id()
    return job_id

@app.route("/buildvm")
def create_vm():

    vmname = request.args.get('vmname')
    job = q.enqueue(build_system, vmname,timeout=600)
    job_id = job.get_id()
    return job_id

@app.route("/results")
@app.route("/results/<string:job_id>")
def get_results(job_id=None):

    if job_id is None:
       return jsonify(queued_job_ids=q.job_ids)

    job = q.fetch_job(job_id)

    if job.is_failed:
        return 'Job has failed!', 400

    if job.is_finished:
        return jsonify(result=job.result)

    return 'Job has not finished!', 202

@app.route("/metrics")
def get_metrics():
    mets('default')
    #return prometheus_client.generate_latest()
    return Response(prometheus_client.generate_latest(), mimetype='text/plain')


if __name__ == '__main__':
    # Start server
    monitor(app, port=8000)
    app.run(host='0.0.0.0', port=5000)
