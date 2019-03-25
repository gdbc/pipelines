import re
import connexion
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


user_env = db.Table('user_env',
    db.Column('user_id', db.Integer, db.ForeignKey('user.user_id')),
    db.Column('env_id', db.Integer, db.ForeignKey('env.env_id'))
)

user_bu = db.Table('user_bu',
    db.Column('user_id', db.Integer, db.ForeignKey('user.user_id')),
    db.Column('bu_id', db.Integer, db.ForeignKey('bu.bu_id'))
)

user_app = db.Table('user_app',
    db.Column('user_id', db.Integer, db.ForeignKey('user.user_id')),
    db.Column('app_id', db.Integer, db.ForeignKey('app.app_id'))
)

user_host = db.Table('user_host',
    db.Column('user_id', db.Integer, db.ForeignKey('user.user_id')),
    db.Column('host_id', db.Integer, db.ForeignKey('host.host_id'))
)

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(20), unique=True
)

class Env(db.Model):
    env_id = db.Column(db.Integer, primary_key=True)
    env_name = db.Column(db.String(20), unique=True)
    env_sub  = db.relationship('User', secondary=user_env, backref=db.backref('envs', lazy='dynamic')
)

class Bu(db.Model):
    bu_id = db.Column(db.Integer, primary_key=True)
    bu_name = db.Column(db.String(20), unique=True)
    bu_sub  = db.relationship('User', secondary=user_bu, backref=db.backref('bus', lazy='dynamic')
)

class App(db.Model):
    app_id = db.Column(db.Integer, primary_key=True)
    app_name = db.Column(db.String(20), unique=True)
    app_sub  = db.relationship('User', secondary=user_app, backref=db.backref('apptype', lazy='dynamic')
)

class Host(db.Model):
    host_id = db.Column(db.Integer, primary_key=True)
    host_name = db.Column(db.String(20), unique=True)
    host_sub  = db.relationship('User', secondary=user_host, backref=db.backref('host', lazy='dynamic')
)


app = connexion.FlaskApp(__name__)
app.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db.app = app.app
db.init_app(app.app)
db.create_all()

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

app_ora = App(app_name='ora')
app_cii = App(app_name='cii')
app_jen = App(app_name='jen')

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
db.session.flush()

#user_id = 'admin'
#user_ev = db.session.query(Env).join(user_env).join(User)
#user_one_env = user_ev.filter_by(user_name=user_id)
#user_env = [y.env_name for y in user_one_env]

#ubu = db.session.query(Bu).join(user_bu).join(User)
#user_one_bu = ubu.filter_by(user_name=user_id)
#user_bu = [b.bu_name for b in user_one_bu]

#appt = db.session.query(App).join(user_app).join(User)
#user_one_app = appt.filter_by(user_name=user_id)
#user_app = [a.app_name for a in user_one_app]


def user_exists(user_id):
   try: 
       users = []
       user = db.session.query(User)
       user_one_user = user.filter_by(user_name=user_id)
       u = [userx.user_name for userx in user_one_user]
       print(u)
       if user_id in u:
           return True
       else:
           return False
   except Exception as e:
       print("Failed, error: %s" %(e))


def fqdn_exists(user_id, fqdn):
   try:
       hosts = []
       u_hosts = db.session.query(Host).join(user_host).join(User)
       user_one_hosts = u_hosts.filter_by(user_name=user_id)
       h = [hostx.host_name for hostx in user_one_hosts]
       if fqdn in h:
           return True
       else:
           return False
   except Exception as e:
       print("Failed, error: %s" %(e))
   

def user_envs(user_id):
   envs = []
   user_ev = db.session.query(Env).join(user_env).join(User)
   user_one_env = user_ev.filter_by(user_name=user_id)
   env_l = [e.env_name for e in user_one_env]
   return env_l


def user_bus(user_id):
   bus = []
   ubu = db.session.query(Bu).join(user_bu).join(User)
   user_one_bu = ubu.filter_by(user_name=user_id)
   bu_l = [b.bu_name for b in user_one_bu]
   return bu_l


def user_apps(user_id):
   appt = db.session.query(App).join(user_app).join(User)
   user_one_app = appt.filter_by(user_name=user_id)
   app_l = [a.app_name for a in user_one_app]
   return app_l


#RBAC

def user_env_role(user_id, fqdn):
   try: 
       env,bu,stype = name_to_path(fqdn)
       user_env_list = user_envs(user_id)
       ub = user_bus(user_id)
       ua = user_app(user_id)
       if env in user_env_list:
           if not ub and not ua:
             return True
           elif bu in ub and stype not in ua: 
             return True
           elif bu in ub and stype in ua:
             return True
           #else:
           #  return False
       else:
           return False
   except Exception as e:
       print("Failed, error: %s" %(e))
     

def user_bu_role(user_id, fqdn):
   try: 
       env,bu,stype = name_to_path(fqdn)
       user_bu_list = user_bus(user_id)
       ue = user_envs(user_id)
       ua = user_app(user_id)
       if bu in user_bu_list: 
           if not ue and not ua:
               return True
           elif env in ue and stype not in ua:
               return True
           elif env in ue and stype in ua:
               return True
           #else:
           #    return False
       else:
           return False

   except Exception as e:
       print("Failed, error: %s" %(e))

def user_apptype_role(user_id, fqdn):
   try:
       env,bu,stype = name_to_path(fqdn)
       user_apptype_list = user_apps(user_id)
       ub = user_bus(user_id)
       ue = user_envs(user_id)
       if env in user_apptype_list:
           if not ub and not ue:
               return True
           elif env in ue and bu not in ub: 
               return True
           elif env in ue and bu in ub:
               return True
       else: 
           return False
   except Exception as e:
       print("Failed, error: %s" %(e))


def get_servertype(alphanum):

    an     = alphanum
    r      = re.compile("([a-zA-Z]+)([0-9]+)")
    stype  = r.match(an)
    return stype.group(1)


def name_to_path(servername):

    sname        = servername.split("-")
    env          = ""
    bu           = sname[1]
    server_type  = get_servertype(sname[2])

    if sname[0][0] == 'q':
      env = "q"
    elif sname[0][0] == 'd':
      env = "d"
    elif sname[0][0] == 'u':
      env = "u"
    elif sname[0][0] == 's':
      env = "s"
    elif sname[0][0] == 'p':
      env = "p"
    else:
      env = "que"

    return env,bu,server_type


# Example 
# x,y,z = name_to_path('dnv-it-lapp0001')
