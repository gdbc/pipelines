from kubernetes import client, config, watch
def main():    
    ns = "inttest1"
    config.load_kube_config()
    api = client.CoreV1Api()
    pvcs = api.list_namespaced_persistent_volume_claim(
      namespace=ns, watch=False)
    print("---- PVCs ---")
    print("%-16s\t%-40s\t%-6s" % ("Name", "Volume", "Size"))
    for pvc in pvcs.items:
        print("%-16s\t%-40s\t%-6s" %
              (pvc.metadata.name, pvc.spec.volume_name,
               pvc.spec.resources.requests['storage']))
main()
