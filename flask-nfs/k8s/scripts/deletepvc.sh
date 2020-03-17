#!/bin/bash

cluster=$1
namespace=$2
pvcname=$3

curl http://192.168.39.179:32000/deletepvcs?token=123asdffdaTGyI123zZ1'&'pvcname="$pvcname"'&'namespace=$namespace'&'cluster=$cluster

echo "curl http://192.168.39.179:32000/deletepvcs?token=123asdffdaTGyI123zZ1'&'pvcname="$pvcname"'&'namespace=$namespace'&'cluster=$cluster"
