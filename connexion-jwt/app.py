#!/usr/bin/env python3
'''
Basic example of a resource server
'''

import six
import time
import base64
import connexion
from auth_db2 import db
from connexion.decorators.security import validate_scope
from connexion.exceptions import OAuthScopeProblem

from jose import JWTError, jwt

JWT_ISSUER = 'com.zalando.connexion'
JWT_SECRET = 'change_this'
JWT_LIFETIME_SECONDS = 600
JWT_ALGORITHM = 'HS256'


def generate_token(user_id):
    timestamp = _current_timestamp()
    payload = {
        "iss": JWT_ISSUER,
        "iat": int(timestamp),
        "exp": int(timestamp + JWT_LIFETIME_SECONDS),
        "sub": str(user_id),
        #"sub": str(12),
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

def ssh():
    headers = connexion.request.headers['Authorization'].split()[1].strip()
    username =  base64.b64encode(base64.b64decode(headers).split(":")[0])
    return userpass

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
