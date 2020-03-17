from kubernetes import client, config, watch
def getpvcs(cluster, namespace):    
    try:
        ns       = namespace
        replystr = ""
        api      = client.CoreV1Api(api_client=config.new_client_from_config(context=cluster))
        pvcs     = api.list_namespaced_persistent_volume_claim(namespace=ns, watch=False)
        replystr = "---- PVCs ---\n"
        replystr += ("%-16s\t%-40s\t%-6s\n" % ("Name", "Volume", "Size"))
        for pvc in pvcs.items:
            replystr += ("%-16s\t%-40s\t%-6s\n" %(pvc.metadata.name, pvc.spec.volume_name,
               pvc.spec.resources.requests['storage']))

        return replystr
    except Exception as e:
        print("error: ", e)
        return '"message": {"error": "Something borked in getpvcs"}"'
