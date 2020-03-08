from kubernetes import client, config, watch
def main():    
    config.load_kube_config()
    api = client.CoreV1Api()
    my_resource = {
    "apiVersion": "v1",
    "kind": "PersistentVolumeClaim",
    "metadata": {
        "name": "inttest2-pvc",
        "namespace": "inttest1"
    },
    "spec": {
        "storageClassName": "slow",
        "accessModes": [
            "ReadWriteMany"
        ],
        "resources": {
            "requests": {
                "storage": "10Gi"
            }
        }
    }
    }
    pvcs = api.create_namespaced_persistent_volume_claim(namespace="inttest1",body=my_resource)
    print(pvcs)
main()
