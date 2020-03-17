from kubernetes import client, config, watch

def dpvc(cluster, namespace, pvcname):    
    try: 
        api   = client.CoreV1Api(api_client=config.new_client_from_config(context=cluster))
        ns    = namespace
        nm    = pvcname 
        dpvcs = api.delete_namespaced_persistent_volume_claim(name=nm,namespace=ns)
        output = str(dpvcs) + "\n"
        return output
    except Exception as e:
        return("Exception: ", str(e))
