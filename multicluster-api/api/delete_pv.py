from kubernetes import client, config, watch

def dpv(pvname):    
    try: 
        config.load_incluster_config()
        api = client.CoreV1Api()
        pvn = pvname
        dpvs = api.delete_persistent_volume(name=pvn)
        output = str(dpvs) + "\n"
        return output
    except Exception as e:
        return("Exception e: ", str(e))