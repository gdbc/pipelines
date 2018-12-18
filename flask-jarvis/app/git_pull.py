import git
import json
from get_vars import my_vars
from pathlib import Path


GIT_DEST   = my_vars('envs')['git_dest']
GIT_USER   = my_vars('creds')['git_user']
GIT_PASS   = my_vars('creds')['git_pass']
GIT_SERVER = my_vars('envs')['git_server']
GIT_REPO   = my_vars('envs')['git_repo']
SOURCE     = "https://" + GIT_USER + ":" + GIT_PASS + "@" + GIT_SERVER + GIT_REPO



def update_git(GIT_DEST, GIT_USER, GIT_PASS, GIT_SERVER, GIT_REPO): 
    try: 
        if Path(GIT_DEST).is_dir():
            repo = git.Repo(GIT_DEST)
            o = repo.remotes.origin
            o.pull()
        else:
            repo = git.Repo.clone_from("https://" + GIT_USER + ":" + GIT_PASS + "@" + GIT_SERVER + GIT_REPO, GIT_DEST)                            
        file = open("/home/flask/pipelines/test.txt","a")
        file.write("hello world\n")
        file.close()
        repo.index.add(["/home/flask/pipelines/test.txt"])
        repo.index.commit("initial commit4")
        repo.remote("origin").push()
    except Exception as e:
        print("update_git Exception Caught: %s" %e)
        return "Exception Caught Updating GIT"
