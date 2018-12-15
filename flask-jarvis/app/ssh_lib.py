import os

from fabric2 import Connection, Config

def ssh_run(servername, cmd, sudo):
    try:
        user    = os.environ['SSH_USER']
        passw   = os.environ['SSH_PASS']
        sudotf  = sudo
        command = cmd
        sname   = servername
        print('user: %s passwd: %s servername: %s'%(user,passw,sname))
        config = Config(overrides={'sudo': {'password': passw}})
        c      = Connection(host=sname, user=user, port=22, config=config, connect_kwargs={"password": passw})
        if sudotf:
            result = c.sudo(command, pty=True, hide='stderr')
            if result.exited == 0:
                print("In SUDO")
                print(result.ok)
                print(result.stdout.strip())
                return result.exited
        else:
            result = c.run(SSH_COMMAND, pty=True, hide='stderr')
            if result.exited == 0:
                print("In NOSUDO")
                print(result.ok)
                print(result.stdout.strip())
                return result.exited
    except Exception as e:
        print("ssh_run Exception Caught: %s" %e)
        return "Exception Caught Clearing Certificate"
