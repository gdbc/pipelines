#!/usr/bin/python

import os
import sys
import paramiko
from prometheus_client import CollectorRegistry, Summary, Gauge, Histogram, Counter, write_to_textfile

registry = CollectorRegistry()

h = Histogram('check_svc_api_call_duration_seconds_histogram', 'Histogram for check_svc function', registry=registry)
h.observe(60)

s = Summary('check_svc_api_call_duration_seconds_summary', 'Summary for check_svc function', registry=registry)
s.observe(60)

c = Counter('check_svc_counter', 'Counter for check_svc function', registry=registry)
c.inc()

g = Gauge('check_svc_counter_gauge', 'Gauge for check_svc function', registry=registry)
g.inc()
g.set_to_current_time()

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

@g.track_inprogress()
@c.count_exceptions()
@h.time()
def check_svc(vmname,svc):
    print("inside check_svc")
    exit_status = ssh_connect(user, passw, vmname, svc)
    return exit_status

with h.time():
    pass

with c.count_exceptions():
    pass

with g.track_inprogress():
    pass

with s.time():
    pass

write_to_textfile('/tmp/api_call_duration_seconds.prom', registry)
