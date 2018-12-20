import os
import sys
from pathlib import Path
from ruamel.yaml import YAML

git_dest = my_vars('envs')['git_dest']
git_repo = my_vars('envs')['git_repo']


def update_yaml(gdest=git_dest, grepo=git_repo, filename, sshgroup):
      
    try:
        spath     = gdest + grepo
        sgroup    = sshgroup
        fname     = filename
        full_path = spath + fname
        temp_file = "/tmp/temp.yaml"
        stream    = open(full_path,'r')
        yaml      = YAML()
        data      = yaml.load(stream)
        if sgroup in data['mgmt::ssh::server_options:AllowGroups']:
            print("%s already exists in %s" %(sgroup, full_path))
            return False
        else:
            data['mgmt::ssh::server_options:AllowGroups'].append(sgroup)
            check_file = Path(temp_file)
            if check_file.is_file():
               os.remove(temp_file)    
               os.remove(full_path)
	    with open(temp_file, 'w') as fp:
               yaml.dump(data, fp)
            with open(temp_file, 'r') as original: data = original.read()
            with open(full_path, 'w') as modified: modified.write("---\n" + data)
            os.remove(temp_file)    
         return True

    except Exception as e:
        print("update_yaml Exception Caught: %s" %e)
        return "Exception Caught updating yaml file"
