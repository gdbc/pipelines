#!/usr/bin/python3.6

import sys
import paramiko

def ssh_command(ssh):
    command = "systemctl status docker"
    ssh.invoke_shell()
    stdin, stdout, stderr = ssh.exec_command(command)
    exit_status = stdout.channel.recv_exit_status()
    print(exit_status)

def ssh_connect(host, user, key):
    try:
        ssh = paramiko.SSHClient()
        print('Calling paramiko')
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=host, username=user, key_filename=key)

        ssh_command(ssh)
    except Exception as e:
        print('Connection Failed')
        print(e)

if __name__=='__main__':
    user = "centos"
    key = "/home/gdbc/.ssh/id_rsa"
    host = sys.argv[1]
    ssh_connect(host, user, key)
