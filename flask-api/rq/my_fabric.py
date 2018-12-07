from fabric2 import Connection, Config

config = Config(overrides={'sudo': {'password': '<password>'}})

c = Connection(host='server', user='test', port=22, config=config, connect_kwargs={"password": "<password>"})
c.sudo('whoami', pty=True, hide='stderr')
c.result
help(c)
