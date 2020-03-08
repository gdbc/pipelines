from kubernetes import client, config, watch
def main():    
    config.load_kube_config()
    api = client.CoreV1Api()
    namespace = "inttest1"
    name = "inttest3-pvc"
    storageclass = "medium"
    my_resource = {
    "apiVersion": "v1",
    "kind": "PersistentVolumeClaim",
    "metadata": {
        "name": name,
        "namespace": namespace
    },
    "spec": {
        "storageClassName": storageclass,
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
