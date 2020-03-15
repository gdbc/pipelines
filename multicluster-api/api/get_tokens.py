import yaml

RBACYAML = "/home/flask/rbac/pv-rbac.yaml"


def hastoken(token, rbackfile=RBACYAML):
   try: 
       rbacfile   = yaml.load(open(rbackfile))
       if token in rbacfile['tokens']:
           return True
       else:
           return False
   except Exception as e:
       print("Error: Check authorizations: ", e)
       return False
