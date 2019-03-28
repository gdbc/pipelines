#!/usr/bin/env python3
'''
Basic example of a resource server
'''

import six
import json
import time
import base64
import connexion
from auth_db2 import db
from auth_db2 import *
from connexion.decorators.security import validate_scope
from connexion.exceptions import OAuthScopeProblem

from jose import JWTError, jwt

JWT_ISSUER = 'com.zalando.connexion'
JWT_SECRET = 'change_this'
JWT_LIFETIME_SECONDS = 600
JWT_ALGORITHM = 'HS256'


def generate_token(username):
    timestamp = _current_timestamp()
    payload = {
        "iss": JWT_ISSUER,
        "iat": int(timestamp),
        "exp": int(timestamp + JWT_LIFETIME_SECONDS),
        "sub": str(username),
    }

    return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)


def basic_auth(username, password, required_scopes=None):
    if username == 'admin' and password == 'secret':
        info = {'sub': 'admin', 'scope': 'secret'}
    elif username == 'foo' and password == 'bar':
        info = {'sub': 'user1', 'scope': ''}
    else:
        # optional: raise exception for custom error response
        return None

    # optional
    if required_scopes is not None and not validate_scope(required_scopes, info['scope']):
        raise OAuthScopeProblem(
                description='Provided user doesn\'t have the required access rights',
                required_scopes=required_scopes,
                token_scopes=info['scope']
            )

    return info


def dummy_func(token):
    return None


def decode_token(token):
    try:
        return jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
    except JWTError as e:
        six.raise_from(Unauthorized, e)


def decode_basic(basic):
   try:
       return base64.b64decode(basic.decode("utf-8")).split(':')[0]
   except Exception as e:
       return "Error: ",e 


def get_secret(user, token_info) -> str:
    token = connexion.request.headers['Authorization'].split()[1]
    return jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])


def get_jwt_user(user, token_info) -> str:
    token = connexion.request.headers['Authorization'].split()[1]
    #json_user = json.dumps(jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM]))
    json_user = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
    return json_user['sub']


def getjwt():
    try:
        headers         = connexion.request.headers['Authorization'].split()[1].strip()
        username        = base64.b64decode(str(headers))
        username_string = username.decode("utf-8").strip().split(":")[0]
        jwt_string      = generate_token(username_string)
        return jwt_string
    except Exception as e:
        return "Error: ",e 

def get_user_envs(user_id):
   envs = []
   user_ev = db.session.query(Env).join(user_env).join(User)
   user_one_env = user_ev.filter_by(user_name=user_id)
   f = open("/tmp/users.txt", "a")
   for g in user_one_env:
      envs.append(g.env_name)
      f.write(g.env_name + "\n")
   f.close()
   env_list = ",".join(envs)
   return env_list

def add_user_envs(user_id, env_id): 
    try:
        user = User.query.filter_by(user_name=user_id).first()
        env = Env.query.filter_by(env_name=env_id).first()
        user.envs.append(env)
        db.session.commit()
        #db.session.flush()
        return "done"
    except Exception as e:
        return "Error: ",e


def del_user_envs(user_id, env_id):
    try:
        user = User.query.filter_by(user_name=user_id).first()
        env = Env.query.filter_by(env_name=env_id).first()
        user.envs.remove(env)
        db.session.commit()
        #db.session.flush()
        return "done"
    except Exception as e:
        return "Error: ",e


def add_user_bus(user_id, bu_id):
    try:
        user = User.query.filter_by(user_name=user_id).first()
        bu = Bu.query.filter_by(bu_name=bu_id).first()
        user.bus.append(bu)
        db.session.commit()
        #db.session.flush() 
        return "done"
    except Exception as e:
        return "Error: ",e

def del_user_bus(user_id, bu_id):
    try:
        user = User.query.filter_by(user_name=user_id).first()
        bu = Bu.query.filter_by(bu_name=bu_id).first()
        user.bus.remove(bu)
        db.session.commit()
        #db.session.flush()
        return "done"
    except Exception as e:
        return "Error: ",e

def add_user_app(user_id, app_id):
    try:
        user = User.query.filter_by(user_name=user_id).first()
        apps = App.query.filter_by(app_name=app_id).first()
        user.apptype.append(apps)
        db.session.commit()
        #db.session.flush()
        return "done"
    except Exception as e:
        return "Error: ",e


def del_user_app(user_id, app_id):
    try:
        user = User.query.filter_by(user_name=user_id).first()
        apps = App.query.filter_by(app_name=app_id).first()
        user.apptype.remove(apps)
        db.session.commit()
        #db.session.flush()
        return "done"
    except Exception as e:
        return "Error: ",e

def add_user_host(user_id, host_id):
    try:
        user = User.query.filter_by(user_name=user_id).first()
        host = Host.query.filter_by(host_name=host_id).first()
        user.host.append(host)
        db.session.commit()
        #db.session.flush()
        return "done"
    except Exception as e:
        return "Error: ",e


def del_user_host(user_id, host_id):
    try:
        user = User.query.filter_by(user_name=user_id).first()
        host = Host.query.filter_by(host_name=host_id).first()
        user.host.remove(host)
        db.session.commit()
        #db.session.flush()
        return "done"
    except Exception as e:
        return "Error: ",e



def user_exists(user_id):
   users = []
   user = db.session.query(User)
   user_one_user = user.filter_by(user_name=user_id)
   u = [userx.user_name for userx in user_one_user]
   if user_id in u:
       return True
   else: 
       return False


def get_user_bus(user_id):
   bus = []
   ubu = db.session.query(Bu).join(user_bu).join(User)
   user_one_bu = ubu.filter_by(user_name=user_id)
   for bu in user_one_bu:
      bus.append(bu.bu_name)
   bu_list = ",".join(bus)
   return bu_list


def get_user_app(user_id):
   apps = []
   appt = db.session.query(App).join(user_app).join(User)
   user_one_app = appt.filter_by(user_name=user_id)
   for app in user_one_app:
      apps.append(app.app_name)
   app_list = ",".join(apps)
   return app_list


def get_user_hosts(user_id):
   hosts = []
   u_hosts = db.session.query(Host).join(user_host).join(User)
   user_one_hosts = u_hosts.filter_by(user_name=user_id)
   for host in user_one_hosts:
      hosts.append(host.host_name)
   host_list = ",".join(hosts)
   return host_list

def get_envs():
    env_list = []
    envs = db.session.query(Env).order_by(Env.env_name)
    for e in envs:
        env_list.append(e.env_name)
    env_list_return = ",".join(env_list)
    return env_list_return

def add_env(env_id):
    try:
        envs = Env(env_name=env_id)
        db.session.add(envs)
        db.session.commit()
        return "done"
    except Exception as e:
        return "Error: ",e

def createdb():

    user1 = User(user_name='admin')
    user2 = User(user_name='graeme')
    user3 = User(user_name='test')

    db.session.add(user1)
    db.session.add(user2)
    db.session.add(user3)

    dev = Env(env_name='d')
    uat = Env(env_name='u')
    prd = Env(env_name='p')

    db.session.add(dev)
    db.session.add(uat)
    db.session.add(prd)
    
    user1.envs.append(dev)
    user2.envs.append(dev)
    user3.envs.append(dev)
    user1.envs.append(uat)
    user2.envs.append(prd)
   
    bu_it = Bu(bu_name='it')
    bu_dt = Bu(bu_name='dt')
    bu_rm = Bu(bu_name='rm')
    db.session.add(bu_it)
    db.session.add(bu_dt)
    db.session.add(bu_rm)

    user1.bus.append(bu_it)
    user2.bus.append(bu_it)
    user3.bus.append(bu_it)
    user1.bus.append(bu_dt)
    user2.bus.append(bu_rm)

    app_ora = App(app_name='lora')
    app_cii = App(app_name='lcii')
    app_jen = App(app_name='ljen')

    user1.apptype.append(app_ora)
    user2.apptype.append(app_ora)
    user3.apptype.append(app_cii)
    user1.apptype.append(app_cii)
    user1.apptype.append(app_jen)
    user2.apptype.append(app_jen)

    host1  = Host(host_name='dnv-it-lapp0001')
    host2  = Host(host_name='unv-it-lapp0001')
    host3  = Host(host_name='qnv-it-lapp0001')
    host4  = Host(host_name='pnv-it-lapp0001')
    host5  = Host(host_name='pnv-it-lora0001')
    host6  = Host(host_name='unv-it-lora0001')
    host7  = Host(host_name='dnv-it-lora0001')
    host8  = Host(host_name='pnv-rm-lapp0001')
    host9  = Host(host_name='dnv-rm-lapp0001')
    host10 = Host(host_name='unv-rm-lapp0001')
    host11 = Host(host_name='unv-rm-lora0001')
    host12 = Host(host_name='pnv-rm-lora0001')

    user1.host.append(host1)
    user1.host.append(host2)
    user1.host.append(host3)
    user1.host.append(host5)
    user1.host.append(host6)
    user1.host.append(host7)
    user1.host.append(host11)
    user1.host.append(host12)

    user2.host.append(host1)
    user2.host.append(host7)

    user3.host.append(host2)
    user3.host.append(host6)
    user3.host.append(host10)
    user3.host.append(host11)

    db.session.commit()
    #db.session.flush()
    
    return "done"
 
def _current_timestamp() -> int:
    return int(time.time())


if __name__ == '__main__':
    app = connexion.FlaskApp(__name__)
    app.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
    db.app = app.app
    db.init_app(app.app)
    db.create_all()
    app.add_api('openapi.yaml')
    app.run(port=8080, debug=True)
