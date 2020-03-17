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
            pvandpvc = ""
            try: 
                if pv.spec.claim_ref.namespace is not None:
                    pvandpvc = pv.spec.claim_ref.namespace + "/" + pv.spec.claim_ref.name
            except Exception as e:
                pvandpvc = "Unassigned"
            replystr += ("%-16s\t%-10s\t%-30s\t%-10s\t%-6s\n" %(pv.metadata.name, pv.status.phase, pvandpvc,pv.spec.storage_class_name,pv.spec.capacity['storage']))
            pvandpvc = ""
        return replystr
    except Exception as e:
        print("error: ", e)
        return '"message": {"error": "something borked in getpvs"}'
