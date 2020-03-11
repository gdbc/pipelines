import yaml

server="192.168.1.67"
mount="/nfs/k8s/inttest1"
#token="123asdffdaTGyI123zZ1"
token="456asdffdaTGyI123zZ1"

def checkrbac(token, svr, mnt, rbackfile="pv-rbac.yaml"):
   try: 
       rbacfile = yaml.load(open(rbackfile))
       if token in rbacfile['tokens']:
           print("here")
           if svr in rbacfile['tokens'][token]['volumes']:
               print("hereW")
               if mnt in rbacfile['tokens'][token]['volumes'][svr]['paths']:
                   return True
               else:
                   return False
           else:
               return False
       else:
           return False
   except Exception as e:
       print("Error: Check authorizations: ", e)
       return False

res = checkrbac(token, server, mount)
print(res)
