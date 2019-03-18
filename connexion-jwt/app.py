#!/usr/bin/env python3
'''
Basic example of a resource server
'''

import six
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
    return '''
    You are user_id {user} and the secret is 'wbevuec'.
    Decoded token claims: {token_info}.
    '''.format(user=user, token_info=token_info)


def getjwt():
    try:
        headers         = connexion.request.headers['Authorization'].split()[1].strip()
        username        = base64.b64decode(str(headers))
        username_string = username.decode("utf-8").strip().split(":")[0]
        jwt_string      = generate_token(username_string)
        return jwt_string
    except Exception as e:
        return "Error: ",e 

def readb():
   group_ev = db.session.query(Env).join(group_env).join(Group)
   group_one_env = group_ev.filter_by(group_name='group_one')
   f = open("/tmp/groups.txt", "a")
   for g in group_one_env:
      f.write(g.env_name + "\n")
   f.close()
   return "hi"

def createdb():

    group1 = Group(group_name='group_one')
    group2 = Group(group_name='group_two')
    group3 = Group(group_name='group_three')

    db.session.add(group1)
    db.session.add(group2)
    db.session.add(group3)

    dev = Env(env_name='d')
    uat = Env(env_name='u')
    prd = Env(env_name='p')

    db.session.add(dev)
    db.session.add(uat)
    db.session.add(prd)
    
    group1.envs.append(dev)
    group2.envs.append(dev)
    group3.envs.append(dev)
    group1.envs.append(uat)
    group2.envs.append(prd)
   
    bu_it = Bu(bu_name='it')
    bu_dt = Bu(bu_name='dt')
    bu_rm = Bu(bu_name='rm')

    db.session.add(bu_it)
    db.session.add(bu_dt)
    db.session.add(bu_rm)

    group1.bus.append(bu_it)
    group2.bus.append(bu_it)
    group3.bus.append(bu_it)
    group1.bus.append(bu_dt)
    group2.bus.append(bu_rm)

    app_ora = App(app_name='ora')
    app_cii = App(app_name='cii')
    app_jen = App(app_name='jen')

    group1.apptype.append(app_ora)
    group2.apptype.append(app_ora)
    group3.apptype.append(app_cii)
    group1.apptype.append(app_cii)
    group1.apptype.append(app_jen)
    group2.apptype.append(app_jen)

    db.session.commit()
    db.session.flush()
    
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
