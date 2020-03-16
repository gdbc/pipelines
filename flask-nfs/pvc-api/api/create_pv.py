from kubernetes import client, config, watch

def cpv(context, pvname, server, path):    
    try: 
        cluster = context
        api = client.CoreV1Api(api_client=config.new_client_from_config(context=cluster))
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
        output = str(pvs) + "\n"
        return output
    except Exception as e:
        return("Exception e: ", str(e))
