import yaml
import json

server="192.168.1.67"
mount="/nfs/k8s/inttest1"
token="123asdffdaTGyI123zZ1"
#token="456asdffdaTGyI123zZ1"

def checkrbac(token, rbackfile="pv-rbac.yaml"):
   try: 
       rbacfile   = yaml.load(open(rbackfile))
       if token in rbacfile['tokens']:
           data   = rbacfile['tokens'][token]
           output = yaml.dump(data)
           return output
       else:
           return '"{"error": "something failed!"}'
   except Exception as e:
       print("Error: Check authorizations: ", e)
       return False

res = checkrbac(token)
print(res)
