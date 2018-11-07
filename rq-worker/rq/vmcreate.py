#!/usr/bin/python

import os
import sys
import time
import paramiko

user = os.environ["SSH_HOST_USER"]
passw = os.environ["SSH_HOST_PASS"]
host = os.environ["SSH_HOST"]
client_user = os.environ['SSH_USER']
client_pass = os.environ['SSH_PASS']

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
        res = ssh_command(ssh, vmname)
        print res
        return res
    except Exception as e:
        print('Connection Failed')
        print(e)

def ssh_vm_up_check(user, passw, vmname):
    try:
        ssh = paramiko.SSHClient()
        print('Calling paramiko')
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=vmname, username=user, password=passw)
        ssh.invoke_shell()
        stdin, stdout, stderr = ssh.exec_command('systemctl status docker')
        exit_status = stdout.channel.recv_exit_status()
        return exit_status
    except Exception as e:
        print('Connection Failed')
        print(e)

def build_system(vmname):
    SSH = True
    TOTAL_WAIT=0
    build_status = ssh_connect(host, user, passw, vmname)
    print("build_status: %s" %build_status)
    if build_status == 0:
        while SSH:
           check_ssh = ssh_vm_up_check(client_user, client_pass, vmname)
           print("Check ssh status: %s" %check_ssh)
           if check_ssh == 0:
              print("Ssh is true!")
              SSH = False
           else:
              print("Sleeping for 10")
              time.sleep(10)
              TOTAL_WAIT+=10
           if TOTAL_WAIT > 300:
              return vmname + "=failed"
    return vmname + "=up"
    
           

