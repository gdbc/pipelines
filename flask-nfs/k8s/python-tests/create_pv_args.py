from kubernetes import client, config, watch
def main():    
    config.load_kube_config()
    api = client.CoreV1Api()
    pvname = "nfs-inttest3"
    server = "192.168.1.67"
    path   = "/nfs/k8s/inttest3"
    my_resource = {
    "apiVersion": "v1",
    "kind": "PersistentVolume",
    "metadata": {
        "name": pvname
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
            "path": path,
            "server": server
        },
        "persistentVolumeReclaimPolicy": "Retain",
        "volumeMode": "Filesystem"
    }

    }

    pvcs = api.create_persistent_volume(body=my_resource)
    print(pvcs)
main()
