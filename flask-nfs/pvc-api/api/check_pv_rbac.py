import yaml
from kubernetes import client, config, watch

#server="192.168.1.67"
#mount="/nfs/k8s/inttest1"
#token="123asdffdaTGyI123zZ1"
#token="456asdffdaTGyI123zZ1"

#This should check for creation and deletion of PVs
RBACYAML = "/home/flask/rbac/pv-rbac.yaml"

def checkpvrbac(cluster, token, svr, mnt, rbackfile=RBACYAML):
   try:
       rbacfile = yaml.load(open(rbackfile))
       if token in rbacfile['tokens']:
           if cluster in rbacfile['tokens'][token]['contexts']:
               if svr in rbacfile['tokens'][token]['contexts'][cluster]['volumes']:
                   if mnt in rbacfile['tokens'][token]['contexts'][cluster]['volumes'][svr]['paths']:
                       return True
                   else:
                       return False
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
#def checkpvcrbac(token, pvcname, rbackfile=RBACYAML):
#   try: 
#       rbacfile = yaml.load(open(rbackfile))
#       if token in rbacfile['tokens']:
#           if svr in rbacfile['tokens'][token]['volumes']:
#               if mnt in rbacfile['tokens'][token]['volumes'][svr]['paths']:
#                   return True
#               else:
#                   return False
#           else:
#               return False
#       else:
#           return False
#   except Exception as e:
#       print("Error: Check authorizations: ", e)
#       return False

def getpv(cluster, namespace, pvcname):
    try:
        pvn      = ""
        ns       = namespace
        pvcn     = pvcname
        config.load_incluster_config()
        api      = client.CoreV1Api()
        pvcs     = api.list_namespaced_persistent_volume_claim(namespace=ns, watch=False)
        for pvc in pvcs.items:
            if str(pvc.metadata.name).strip() == str(pvcn).strip():
                pvn = pvc.spec.volume_name
                return pvn
        return "No pv found for pvc: ", pvcn
    except Exception as e:
       print("Error: something failed in getpv", e)
       return "failed" 

def getpvnfsinfo(cluster, token, pv):
    try:
        config.load_incluster_config()
        pvn = pv
        api = client.CoreV1Api()
        pvs = api.list_persistent_volume()
        srv = "none"
        mnt = "none"
        for pv in pvs.items:
            if pv.metadata.name == pvn:
                if pv.spec.nfs is not None:
                    srv = pv.spec.nfs.server
                    mnt = pv.spec.nfs.path
                else:
                    return("pv is not nfs volume!")
        return srv, mnt
    except Exception as e:
       print("Error: something failed in getpvnfsinfo", e)
       return "failed" 


