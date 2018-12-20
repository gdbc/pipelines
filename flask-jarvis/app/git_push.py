import git
import json
from get_vars import my_vars
from pathlib import Path


git_dest    = my_vars('envs')['git_dest']
git_user    = my_vars('creds')['git_user']
git_pass    = my_vars('creds')['git_pass']
git_server  = my_vars('envs')['git_server']
git_repo    = my_vars('envs')['git_repo']
git_source  = "https://" + git_user + ":" + git_pass + "@" + git_server + git_repo
git_comment = "this is a test commit"
git_file    = "/test.txt"


def push_git(gsource, fullpath, comment=git_comment): 
    try: 
        gs       = gsource
        fpath    = fullpath
        gcomment = git_comment
        repo     = git.Repo(gs)
        if not repo.is_dirt():
            repo.index.add([fpath])
            repo.index.commit(IT_COMMENT)
            repo.remote("origin").push()
            return True 
        else:
            return False
    except Exception as e:
        print("push_git Exception Caught: %s" %e)
        return "Exception Caught pushing to GIT"
