#!/usr/bin/python

import os
import sys
import paramiko

user = os.environ["SSH_HOST_USER"]
passw = os.environ["SSH_HOST_PASS"]
host = os.environ["SSH_HOST"]

def ssh_command(ssh, vmname):
    command = "/home/gdbc/virt/kvm-install-vm create -c 2 -m 2048 -d 20 " + vmname
    ssh.invoke_shell()
    stdin, stdout, stderr = ssh.exec_command(command)
    exit_status = stdout.channel.recv_exit_status()
    print exit_status
    return exit_status

def ssh_connect(host, user, passw, vmname):
    try:
        ssh = paramiko.SSHClient()
        print('Calling paramiko')
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=host, username=user, password=passw)
        ssh_command(ssh, vmname)
    except Exception as e:
        print('Connection Failed')
        print(e)

def build_system(vmname):

    ssh_connect(host, user, passw, vmname)
