from ruamel.yaml import YAML
import sys

SSH_GROUP='test-group'
SSH_GROUP1='test-group2'
INFNAME = "example.yaml"
OUTFNAME="output.yml"

fname=INFNAME
stream=open(fname,'r')
yaml = YAML()
data=yaml.load(stream)
data['mgmt::ssh::server_options:AllowGroups'].append(SSH_GROUP)
data['mgmt::ssh::server_options:AllowGroups'].append(SSH_GROUP1)
with open(OUTFNAME, 'w') as fp:
    yaml.dump(data, fp)

with open(OUTFNAME, 'r') as original: data = original.read()
with open(OUTFNAME, 'w') as modified: modified.write("---\n" + data)
