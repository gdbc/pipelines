#!/bin/bash

cluster=$1

#curl http://localhost:5001/getpvs?token=123asdffdaTGyI123zZ1'&'cluster=k1

curl http://192.168.39.179:32000/getpvs?token=123asdffdaTGyI123zZ1'&'cluster=$cluster
echo "curl http://192.168.39.179:32000/getpvs?token=123asdffdaTGyI123zZ1'&'cluster=$cluster"


