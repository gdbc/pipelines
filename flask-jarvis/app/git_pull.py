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


def pull_git(GIT_DEST=git_dest, GIT_SOURCE=git_source, GIT_REPO=git_repo, GIT_FILE=git_file, GIT_COMMENT=git_comment): 
    try: 
        if Path(GIT_DEST + GIT_REPO).is_dir():
            repo = git.Repo(GIT_DEST + GIT_REPO)
            o = repo.remotes.origin
            o.pull()
        else:
            repo = git.Repo.clone_from(GIT_SOURCE, GIT_DEST + GIT_REPO)
        if not repo.is_dirt():
            return True
        else: 
            return False

        #file = open(GIT_DEST + GIT_REPO + GIT_FILE,"a")
        #file.write("hello w0rld\n")
        #file.close()
        #repo.index.add([GIT_DEST + GIT_REPO + GIT_FILE])
        #repo.index.commit(GIT_COMMENT)
        #repo.remote("origin").push()
        #y = repo.remote("origin").push()
        #print("y: %s" %y)
    except Exception as e:
        print("update_git Exception Caught: %s" %e)
        return "Exception Caught Updating GIT"
