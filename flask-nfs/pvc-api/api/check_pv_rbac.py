import yaml
from kubernetes import client, config, watch

#server="192.168.1.67"
#mount="/nfs/k8s/inttest1"
#token="123asdffdaTGyI123zZ1"
#token="456asdffdaTGyI123zZ1"

#This should check for creation and deletion of PVs
def checkpvrbac(token, svr, mnt, rbackfile="pv-rbac.yaml"):
   try: 
       rbacfile = yaml.load(open(rbackfile))
       if token in rbacfile['tokens']:
           if svr in rbacfile['tokens'][token]['volumes']:
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

#This should check for creation and deletion of pvcs
def checkpvcrbac(token, pvcname, rbackfile="pv-rbac.yaml"):
   try: 
       rbacfile = yaml.load(open(rbackfile))
       if token in rbacfile['tokens']:
           if svr in rbacfile['tokens'][token]['volumes']:
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

def getpv(namespace, pvcname):
    try:
        pvn      = ""
        ns       = namespace
        pvcn     = pvcname
        config.load_kube_config()
        api      = client.CoreV1Api()
        pvcs     = api.list_namespaced_persistent_volume_claim(namespace=ns, watch=False)
        for pvc in pvcs.items:
            if str(pvc.metadata.name).strip() == str(pvcn).strip():
                pvn = pvc.spec.volume_name
                return pvn
        return "No pv found for pvc: ", pvcn
    except Exception as e:
       print("Error: Check authorizations: ", e)
       return "failed" 



