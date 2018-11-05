#!/usr/bin/python

import os
import sys
import paramiko

def ssh_command(ssh):
    command = "/home/gdbc/virt/kvm-install-vm create -c 2 -m 2048 -d 20 foo"
    ssh.invoke_shell()
    stdin, stdout, stderr = ssh.exec_command(command)
    exit_status = stdout.channel.recv_exit_status()
    print(exit_status)

def ssh_connect(host, user, passw):
    try:
        ssh = paramiko.SSHClient()
        print('Calling paramiko')
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=host, username=user, password=passw)

        ssh_command(ssh)
    except Exception as e:
        print('Connection Failed')
        print(e)

if __name__=='__main__':
    user = os.environ["SSH_USER"]
    passw = os.environ["SSH_PASS"]
    host = os.environ["SSH_HOST"]
    ssh_connect(host, user, passw)
