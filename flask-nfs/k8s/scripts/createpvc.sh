#!/bin/bash

cluster=$1
pvname=$2
pvcname=$3
namespace=$4

curl http://192.168.39.179:32000/createpvcs?token=123asdffdaTGyI123zZ1'&'pvname=$pvname'&'pvcname=$pvcname'&'namespace=$namespace'&'cluster=$cluster

echo "curl http://192.168.39.179:32000/createpvcs?token=123asdffdaTGyI123zZ1'&'pvname=$pvname'&'pvcname=$pvcname'&'namespace=$namespace"
