from kubernetes import client, config, watch
def main():    
    config.load_kube_config()
    api = client.CoreV1Api()
    namespace = "inttest1"
    name = "inttest3-pvc"

    pvcs = api.delete_namespaced_persistent_volume_claim(name=name,namespace=namespace)
    print(pvcs)
main()
