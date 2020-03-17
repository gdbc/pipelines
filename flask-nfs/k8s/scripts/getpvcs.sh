#!/bin/bash

cluster=$1
namespace=$2


curl http://192.168.39.179:32000/getpvcs?token=123asdffdaTGyI123zZ1'&'namespace=$namespace'&'cluster=$cluster

echo "curl http://192.168.39.179:32000/getpvcs?token=123asdffdaTGyI123zZ1'&'namespace=$namespace'&'cluster=$cluster"
