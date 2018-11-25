#!/usr/bin/python

import os
import sys
import paramiko
from prometheus_client import CollectorRegistry, Summary, Gauge, Histogram, Counter, write_to_textfile

registry = CollectorRegistry()

#h = Histogram('check_svc_api_call_duration_seconds_histogram', 'Histogram for check_svc function', registry=registry)
#h.observe(5)

#s = Summary('check_svc_api_call_duration_seconds_summary', 'Summary for check_svc function', registry=registry)
#s.observe(5)

#c = Counter('check_svc_counter', 'Counter for check_svc function', ['method', 'endpoint'], registry=registry)
#g = Gauge('check_svc_gauge', 'Gauge for check_svc function',['method', 'endpoint'], registry=registry)


user  = os.environ["SSH_USER"]
passw = os.environ["SSH_PASS"]
#host = os.environ["SSH_HOST"]

def ssh_command(ssh, svc):
    command = "systemctl status " + svc
    ssh.invoke_shell()
    stdin, stdout, stderr = ssh.exec_command(command)
    exit_status = stdout.channel.recv_exit_status()
    return exit_status

def ssh_connect(user, passw, vmname, svc):
    try:
        ssh = paramiko.SSHClient()
        print('Calling paramiko')
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=vmname, username=user, password=passw, look_for_keys=False)
        ex = ssh_command(ssh,svc)
        return ex
    except Exception as e:
        print('Connection Failed')
        print(e)
#@s.time()
#@h.time()
def check_svc(vmname,svc):
    label_dict = {"method": 'check_svc', "endpoint":'checkservice'}
    #c.labels(**label_dict).inc(1)
    #g.labels(**label_dict).inc(1)
    write_to_textfile('/data/api_call_duration_seconds.prom', registry)
    exit_status = ssh_connect(user, passw, vmname, svc)
    return exit_status


