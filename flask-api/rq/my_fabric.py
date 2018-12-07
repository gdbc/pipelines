from fabric2 import Connection, Config

config = Config(overrides={'sudo': {'password': 'test'}})

c = Connection(host='server', user='test', port=22, config=config, connect_kwargs={"password": "test"})
result = c.sudo('whoami', pty=True, hide='stdout')
print(result.exited)
print(result.ok)
#print(result.stdout.strip())
