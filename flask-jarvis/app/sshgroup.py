from convert_hname import *
from update_sshgroup import *
from get_vars import my_vars
from git_pull import pull_git
from git_push import push_git

git_dest = my_vars('envs')['git_dest']
git_repo = my_vars('envs')['git_repo']

def addgroup(servername, sshgroup, gdest=git_dest, grepo=git_repo):

    try:
        sname   = servername
        path    = name_to_path(sname)
        spath   = gdest + grepo
        sgroup  = sshgroup
        if "que" in path:
            print("couldn't resolve hiera path from servername!")
            return False
        fpath   = spath + path
        comment = "Successfully added %s to %s" %(sgroup, fpath)
        if pull_git():
            update_success = update_yaml(fpath, sgroup)
            if update_success:
                print("Updated %s successfully" %fpath)
                if push_git(spath, fpath, comment):
                    print("Successfully added %s to %s" %(sgroup, fpath))
                    return True
            else:
                print("Update %s failed" %fpath)
        else:
            print("Couldn't git pull successfully, could be dirty?")

    except Exception as e:
        print("addgroup Exception Caught: %s" %e)
        return "Exception Caught trying to add group"
