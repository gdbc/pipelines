import re
import connexion
from auth_db2 import *
from auth_db2 import db
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def user_exists(user_id):
   try: 
       users = []
       user = db.session.query(User)
       user_one_user = user.filter_by(user_name=user_id)
       u = [userx.user_name for userx in user_one_user]
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


def user_env_role(user_id, fqdn):
   try: 
       env,bu,stype = name_to_path(fqdn)
       user_env_list = user_envs(user_id)
       ub = user_bus(user_id)
       ua = user_apps(user_id)
       if env in user_env_list:
           if not ub and not ua:
             print("user_bus and user_apps empty for user %s" %(user_id))
             return True
           elif bu in ub and stype not in ua: 
             print("bu: %s exists in user_bus and user_apps empty for user %s" %(bu, user_id))
             return True
           elif bu in ub and stype in ua:
             print("bu: %s exists in user_bus and stype: %s exists in user_apps for user %s" %(bu, stype, user_id))
             return True
       else:
           return False
   except Exception as e:
       print("Failed, error: %s" %(e))
     

def user_bu_role(user_id, fqdn):
   try: 
       env,bu,stype = name_to_path(fqdn)
       user_bu_list = user_bus(user_id)
       ue = user_envs(user_id)
       ua = user_apps(user_id)
       if bu in user_bu_list: 
           if not ue and not ua:
               print("user_envs and user_apps empty for user %s" %(user_id))
               return True
           elif env in ue and stype not in ua:
               print("env: %s exists in user_envs and user_apps empty for user %s" %(env, user_id))
               return True
           elif env in ue and stype in ua:
               print("env: %s exists in user_envs and stype: %s exists in user_apps for user %s" %(env, stype, user_id))
               return True
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
               print("user_bus and user_env empty for user %s" %(user_id))
               return True
           elif env in ue and bu not in ub: 
               print("env: %s exists in user_envs and user_bus empty for user %s" %(env, user_id))
               return True
           elif env in ue and bu in ub:
               print("env: %s exists in user_envs and bu: %s exists in user_bus for user %s" %(env, bu, user_id))
               return True
       else: 
           return False
   except Exception as e:
       print("Failed, error: %s" %(e))


def check_auth(user_id, fqdn):
    try: 
        user_has_access = False
        if user_exists(user_id):
            if fqdn_exists(user_id, fqdn):
                print("fqdn: %s exists for user: %s" %(fqdn, user_id))
                user_has_access = True
            elif user_env_role(user_id,fqdn) and user_has_access == False:
                print("env exists for fqdn: %s and user: %s" %(fqdn, user_id))
                user_has_access = True
            elif user_bu_role(user_id, fqdn) and user_has_access == False:
                print("bu exists for fqdn: %s and user: %s" %(fqdn, user_id))
                user_has_access = True
            elif user_apptype_role(user_id, fqdn) and user_has_access == False:
                print("apptype exists for fqdn: %s and user: %s" %(fqdn, user_id))
                user_has_access = True
            else:
                print("user: %s does not have the correct authorization to edit fqdn: %s" %(user_id, fqdn))
                user_has_access = False
                
        else:
            user_has_access = False
        return user_has_access
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
