from kubernetes import client, config, watch
def getpvcs(namespace):    
    ns       = namespace
    replystr = ""
    config.load_kube_config()
    api      = client.CoreV1Api()
    pvcs     = api.list_namespaced_persistent_volume_claim(namespace=ns, watch=False)
    replystr = "---- PVCs ---\n"
    replystr += ("%-16s\t%-40s\t%-6s\n" % ("Name", "Volume", "Size"))
    for pvc in pvcs.items:
        replystr += ("%-16s\t%-40s\t%-6s" %(pvc.metadata.name, pvc.spec.volume_name,
               pvc.spec.resources.requests['storage']))

    return replystr
r = getpvcs("inttest1")
print(r)
