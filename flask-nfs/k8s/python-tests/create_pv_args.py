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
        #"name": "nfs-inttest2"
        "name": pvname
    },
    "spec": {
        "storageClassName": "medium",
        "capacity": {
            "storage": "10Gi"
        },
        "accessModes": [
            "ReadWriteMany"
        ],
        "nfs": {
            "server": server,
            "path": path
        }
    }
    }



    pvcs = api.create_persistent_volume(body=my_resource)
    print(pvcs)
main()
