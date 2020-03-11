from kubernetes import client, config, watch

def dpvc(namespace, pvcname):    
    try: 
        config.load_incluster_config()
        api   = client.CoreV1Api()
        ns    = namespace
        nm    = pvcname 
        dpvcs = api.delete_namespaced_persistent_volume_claim(name=nm,namespace=ns)
        return str(dpvcs + "\n") 
    except Exception as e:
        return("Exception: ", str(e))
