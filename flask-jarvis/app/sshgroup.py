from git_pull import pull_git

def addgroup(servername, sshgroup):
      if pull_git():
         return True
