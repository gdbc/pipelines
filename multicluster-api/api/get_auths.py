import yaml

RBACYAML = "/home/flask/rbac/pv-rbac.yaml"

def getrbac(token, rbackfile=RBACYAML):
   try: 
       rbacfile   = yaml.load(open(rbackfile))
       if token in rbacfile['tokens']:
           data   = rbacfile['tokens'][token]
           output = yaml.dump(data)
           return output
       else:
           return '"{"error": "something failed in getrbac"}'
   except Exception as e:
       print("Error: Check authorizations: ", e)
       return '"{"error": "something failed in getrbac"}'
