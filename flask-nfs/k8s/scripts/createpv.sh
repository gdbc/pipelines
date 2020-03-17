#!/bin/bash

cluster=$1 
pvname=$2
nfsserver=$3
path=$4

curl http://192.168.39.179:32000/createpvs?token=123asdffdaTGyI123zZ1'&'pvname=$pvname'&'nfsserver=$nfsserver'&'path=$path'&'cluster=$cluster
echo "http://192.168.39.179:32000/createpvs?token=123asdffdaTGyI123zZ1'&'pvname=$pvname'&'nfsserver=$nfsserver'&'path=$path'&'cluster=$cluster"


#curl http://192.168.39.179:32000/createpvs?token=123asdffdaTGyI123zZ1&pvname="pv-inttest1"&nfsserver="192.168.1.67"&path="/nfs/k8s/inttest1"
