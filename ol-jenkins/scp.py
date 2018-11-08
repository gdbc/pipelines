#!/usr/bin/python
import os
import paramiko


hostname = os.environ['SSH_HOST']
password = os.environ['SSH_HOST_PASS'] 
username = os.environ['SSH_HOST_USER']
port = 22

localpath='/tmp/id_rsa'
remotepath='/home/' + username + '/.ssh/id_rsa'

t = paramiko.Transport((hostname, 22))
t.connect(username=username, password=password)
sftp = paramiko.SFTPClient.from_transport(t)
sftp.get(remotepath,localpath)
