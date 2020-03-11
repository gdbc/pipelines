from kubernetes import client, config, watch

def cpv(pvname, server, path):    
    try: 
        config.load_incluster_config()
        api = client.CoreV1Api()
        pvn    = pvname
        srv    = server
        pth    = path

        my_resource = {
        "apiVersion": "v1",
        "kind": "PersistentVolume",
        "metadata": {
            "name": pvn
        },
        "spec": {
            "storageClassName": "standard",
            "accessModes": [
                "ReadWriteMany",
                "ReadWriteOnce",
                "ReadOnlyMany"
            ],
            "capacity": {
                "storage": "10Gi"
            },
            "mountOptions": [
                "vers=4"
            ],
            "nfs": {
                "path": pth,
                "server": srv
            },
            "persistentVolumeReclaimPolicy": "Retain",
            "volumeMode": "Filesystem"
        }

        }

        pvs = api.create_persistent_volume(body=my_resource)
        return str(pvs + "\n")
    except Exception as e:
        return("Exception e: ", str(e))
