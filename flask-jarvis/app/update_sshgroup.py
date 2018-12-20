import os
import sys
from pathlib import Path
from ruamel.yaml import YAML
from get_vars import my_vars

git_dest = my_vars('envs')['git_dest']
git_repo = my_vars('envs')['git_repo']


def update_yaml(filename, sshgroup):
      
    try:
        print("in update_yaml")
        sgroup    = sshgroup
        fname     = filename
        print("fullPath: %s" %fname)
        temp_file = "/tmp/temp.yaml"
        stream    = open(fname,'r')
        yaml      = YAML()
        data      = yaml.load(stream)
        print("data: %s" %data)
        if sgroup in data['mgmt::ssh::server_options:AllowGroups']:
            print("%s already exists in %s" %(sgroup, fname))
            return False
        else:
            data['mgmt::ssh::server_options:AllowGroups'].append(sgroup)
            check_file = Path(temp_file)
            if check_file.is_file():
               os.remove(temp_file)    
               os.remove(fname)
	    with open(temp_file, 'w') as fp:
               yaml.dump(data, fp)
            with open(temp_file, 'r') as original: data = original.read()
            with open(fname, 'w') as modified: modified.write("---\n" + data)
            os.remove(temp_file)    
        return True

    except Exception as e:
        print("update_yaml Exception Caught: %s" %e)
        return "Exception Caught updating yaml file"
