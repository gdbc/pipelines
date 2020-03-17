#!/bin/bash

cluster=$1
pvname=$2


curl http://192.168.39.179:32000/deletepvs?token=123asdffdaTGyI123zZ1'&'pvname="$pvname"'&'cluster=$cluster

echo "curl http://192.168.39.179:32000/deletepvs?token=123asdffdaTGyI123zZ1'&'pvname="$pvname"'&'cluster=$cluster"

#curl http://localhost:5001/deletepvs?token=123asdffdaTGyI123zZ1'&'pvname="pv-inttest1"'&'cluster=minikube

#curl http://192.168.39.179:32000/createpvs?token=123asdffdaTGyI123zZ1&pvname="pv-inttest1"&nfsserver="192.168.1.67"&path="/nfs/k8s/inttest1"
