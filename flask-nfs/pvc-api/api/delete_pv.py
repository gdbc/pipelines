from kubernetes import client, config, watch

def dpv(cluster, pvname):    
    try: 
        api = client.CoreV1Api(api_client=config.new_client_from_config(context=cluster))
        pvn = pvname
        dpvs = api.delete_persistent_volume(name=pvn)
        output = str(dpvs) + "\n"
        return output
    except Exception as e:
        return("Exception e: ", str(e))
