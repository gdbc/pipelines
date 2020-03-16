from kubernetes import client, config, watch
def getpvs(context):    
    try: 
        replystr = ""
        cluster = context
        api      = client.CoreV1Api(api_client=config.new_client_from_config(context=cluster))
        pvs      = api.list_persistent_volume()
        replystr += ("---- PVCs ---\n")
        replystr += ("%-16s\t%-10s\t%-30s\t%-10s\t%-6s\n" % ("NAME", "STATUS", "CLAIM", "STORAGECLASS", "SIZE"))
        for pv in pvs.items:
            replystr += ("%-16s\t%-10s\t%-30s\t%-10s\t%-6s\n" %(pv.metadata.name, pv.status.phase,pv.spec.claim_ref.namespace + "/" + pv.spec.claim_ref.name,pv.spec.storage_class_name,pv.spec.capacity['storage']))
        return replystr
    except Exception as e:
        print("error: ", e)
        return '"message": {"error": "something borked in getpvs"}'
