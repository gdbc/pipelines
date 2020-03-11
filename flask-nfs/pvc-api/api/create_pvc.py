from kubernetes import client, config, watch

def cpvc(namespace, pvcname, pvname):    
    try:   
        config.load_incluster_config()
        api = client.CoreV1Api()
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
        return str(pvcs + "\n")
    except Exception as e:
        return("Exception: ", str(e))
