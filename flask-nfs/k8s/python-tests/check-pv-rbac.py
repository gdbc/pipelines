import yaml

server="192.168.1.67"
mount="/nfs/k8s/inttest1"

def checkrbac(svr, mnt, rbackfile="pv-rbac.yaml"):
   try: 
       rbacfile = yaml.load(open(rbackfile))
       if svr in rbacfile['volumes']:
           print("here")
           print("paths: %s", rbacfile['volumes'][svr]['paths'])
           if mnt in rbacfile['volumes'][svr]['paths']:
               print("here1")
               return True
           else:
               return False
       else:
           return True
   except Exception as e:
       print("Error: Check authorizations: ", e)
       return False

checkrbac(server, mount)
