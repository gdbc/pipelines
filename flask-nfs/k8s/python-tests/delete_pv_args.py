from kubernetes import client, config, watch
def main():    
    config.load_kube_config()
    api = client.CoreV1Api()
    pvname = "nfs-inttest3"

    pvcs = api.delete_persistent_volume(name=pvname)
    print(pvcs)
main()
