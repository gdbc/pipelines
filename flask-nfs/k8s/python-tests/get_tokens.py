import yaml


def hastoken(token, rbackfile="pv-rbac.yaml"):
   try: 
       rbacfile   = yaml.load(open(rbackfile))
       if token in rbacfile['tokens']:
           return True
       else:
           return False
   except Exception as e:
       print("Error: Check authorizations: ", e)
       return False

t = hastoken(token)
print(t)
