#!/usr/bin/python
import sys
import paramiko


hostname = sys.argv['SSH_HOST']
password = sys.argv['SSH_HOST_PASS'] 
username = sys.argv['SSH_HOST_USER']
port = 22

localpath='/tmp/id_rsa'
remotepath='/home/' + username + '/.ssh/id_rsa'

t = paramiko.Transport((hostname, 22))
t.connect(username=username, password=password)
sftp = paramiko.SFTPClient.from_transport(t)
sftp.get(remotepath,localpath)
