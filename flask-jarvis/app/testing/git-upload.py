import git
from pathlib import Path

DEST   = '/home/flask/pipelines'
USER   = '<user>'
PASS   = '<password>'
SERVER = 'github.com'
REPO   = '/gdbc/pipelines'
SOURCE = "https://" + USER + ":" + PASS + "@" + SERVER + REPO

if Path(DEST).is_dir():
    repo = git.Repo(DEST)
    o = repo.remotes.origin
    o.pull()
else:
    repo = git.Repo.clone_from("https://" + USER + ":" + PASS + "@" + SERVER + REPO, DEST)                            
file = open("/home/flask/pipelines/test.txt","a")
file.write("hello world\n")
file.close()
repo.index.add(["/home/flask/pipelines/test.txt"])
repo.index.commit("initial commit4")
repo.remote("origin").push()
