import re

#filepath == "hieradata/<BU>/<servertype>/<env>
#eg       == "hieradata/it/lspli/{test,dev,uat,prd}.yaml


def get_servertype(alphanum):

    an     = alphanum
    r      = re.compile("([a-zA-Z]+)([0-9]+)")
    stype  = r.match(an)
    return stype.group(1)


def name_to_path(servername):

    sname        = servername.split("-")
    base         = "hieradata/"
    env          = ""
    bu           = sname[1] 
    server_type  = get_servertype(sname[2])

    if sname[0][0] == 'q':
      env = "test" 
    elif sname[0][0] == 'd':
      env = "dev" 
    elif sname[0][0] == 'u':
      env = "uat" 
    elif sname[0][0] == 's':
      env = "stage" 
    elif sname[0][0] == 'p':
      env = "prod" 
    else:
      env = "que"

    path = base + bu + "/" + server_type + "/" + env + ".yaml"
    return path
