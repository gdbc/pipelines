#!/usr/bin/python3.4

import prometheus_client
from flask import Flask, jsonify, request, Response
from redis import StrictRedis
from rq import Queue
from sums import add
from sshgroup import addgroup
from ssh_lib import ssh_run
from flask_prometheus import monitor 
from get_mets import mets
from prometheus_client import Summary
from random import randrange

REDIS_HOST="172.17.0.1"
REDIS_PORT="6379"

CONTENT_TYPE_LATEST = str('text/plain; version=0.0.4; charset=utf-8')
#REQUEST_TIME = Summary('summary_request_processing_seconds', 'Time spent processing request')


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

@app.route("/addsshgroup")
def addsshgroup():
    sname    = request.args.get('servername')
    sshgroup = request.args.get('sshgroup')
    result   = addgroup(sname, sshgroup)
    if result == True:
       return "working"
    else:
       return "failed"

@app.route("/testssh")
def create_vm():
    sname = request.args.get('servername')
    command = "yum install httpd -y"
    result = ssh_run(sname, command, True)
    if result == 0:
       return "working"
    else:
       return "failed"


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
