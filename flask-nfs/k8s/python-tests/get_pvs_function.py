from kubernetes import client, config, watch
def getpv():    

    replystr = ""
    config.load_kube_config()
    api      = client.CoreV1Api()
    pvs      = api.list_persistent_volume()
    replystr += ("---- PVCs ---\n")
    replystr += ("%-16s\t%-10s\t%-30s\t%-10s\t%-6s\n" % ("NAME", "STATUS", "CLAIM", "STORAGECLASS", "SIZE"))
    for pv in pvs.items:
        replystr += ("%-16s\t%-10s\t%-30s\t%-10s\t%-6s\n" %(pv.metadata.name, pv.status.phase,pv.spec.claim_ref.namespace + "/" + pv.spec.claim_ref.name,pv.spec.storage_class_name,pv.spec.capacity['storage']))
        #print(pv.metadata.name)
        #print(pv.status.phase)
        #print(pv.spec.claim_ref.namespace + "/" + pv.spec.claim_ref.name)
        #print(pv.spec.storage_class_name)
        #print(pv.spec.capacity['storage'])
    return replystr
r = getpv()
print(r)
