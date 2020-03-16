from kubernetes import client, config, watch

def cpvc(context, namespace, pvcname, pvname):    
    try:   
        cluster = context
        api = client.CoreV1Api(api_client=config.new_client_from_config(context=cluster))
        ns  = namespace
        nm  = pvcname
        vn  = pvname

        my_resource = {
        "apiVersion": "v1",
        "kind": "PersistentVolumeClaim",
        "metadata": {
            "name": nm,
            "namespace": ns
        },
        "spec": {
            "volumeName": vn,
            "accessModes": [
                 "ReadWriteMany"
            ],
            "resources": {
                "requests": {
                    "storage": "1Gi"
                }
            }
        }

        }
        pvcs = api.create_namespaced_persistent_volume_claim(namespace=ns,body=my_resource)
        output = str(pvcs) + "\n"
        return output
    except Exception as e:
        return("Exception: ", str(e))
