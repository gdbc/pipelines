#!/usr/bin/env python3

from auth_db2 import db
from auth_db2 import *

def add_user_envs(user_id, env_id):
    try:
        user = User.query.filter_by(user_name=user_id).first()
        env = Env.query.filter_by(env_name=env_id).first()
        user.envs.append(env)
        db.session.commit()
        db.session.flush()
        return "done"
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

def del_user_envs(user_id, env_id):
    try:
        user = User.query.filter_by(user_name=user_id).first()
        env = Env.query.filter_by(env_name=env_id).first()
        user.envs.remove(env)
        db.session.commit()
        return "done"
    except Exception as e:
        return "Error: ",e

def add_user_bus(user_id, bu_id):
    try:
        user = User.query.filter_by(user_name=user_id).first()
        bu = Bu.query.filter_by(bu_name=bu_id).first()
        user.bus.append(bu)
        db.session.commit()
        return "done"
    except Exception as e:
        return "Error: ",e

def del_user_bus(user_id, bu_id):
    try:
        user = User.query.filter_by(user_name=user_id).first()
        bu = Bu.query.filter_by(bu_name=bu_id).first()
        user.bus.remove(bu)
        db.session.commit()
        return "done"
    except Exception as e:
        return "Error: ",e

def add_user_app(user_id, app_id):
    try:
        user = User.query.filter_by(user_name=user_id).first()
        apps = App.query.filter_by(app_name=app_id).first()
        user.apptype.append(apps)
        db.session.commit()
        return "done"
    except Exception as e:
        return "Error: ",e

def del_user_app(user_id, app_id):
    try:
        user = User.query.filter_by(user_name=user_id).first()
        apps = App.query.filter_by(app_name=app_id).first()
        user.apptype.remove(apps)
        db.session.commit()
        return "done"
    except Exception as e:
        return "Error: ",e

def add_user_host(user_id, host_id):
    try:
        user = User.query.filter_by(user_name=user_id).first()
        host = Host.query.filter_by(host_name=host_id).first()
        user.host.append(host)
        db.session.commit()
        return "done"
    except Exception as e:
        return "Error: ",e

def get_user_hosts(user_id):
   hosts = []
   u_hosts = db.session.query(Host).join(user_host).join(User)
   user_one_hosts = u_hosts.filter_by(user_name=user_id)
   for host in user_one_hosts:
      hosts.append(host.host_name)
   host_list = ",".join(hosts)
   return host_list

def del_user_host(user_id, host_id):
    try:
        user = User.query.filter_by(user_name=user_id).first()
        host = Host.query.filter_by(host_name=host_id).first()
        user.host.remove(host)
        db.session.commit()
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

def get_bus():
    bus_list = []
    bus = db.session.query(Bu).order_by(Bu.bu_name)
    for b in bus:
        bus_list.append(b.bu_name)
    bus_list_return = ",".join(bus_list)
    return bus_list_return

def add_bus(bu_id):
    try:
        bus = Bu(bu_name=bu_id)
        db.session.add(bus)
        db.session.commit()
        return "done"
    except Exception as e:
        return "Error: ",e

def get_apps():
    apps_list = []
    apps = db.session.query(App).order_by(App.app_name)
    for a in apps:
        apps_list.append(a.app_name)
    apps_list_return = ",".join(apps_list)
    return apps_list_return

def add_apps(app_id):
    try:
        apps = App(app_name=app_id)
        db.session.add(apps)
        db.session.commit()
        return "done"
    except Exception as e:
        return "Error: ",e

def get_hosts():
    hosts_list = []
    hosts = db.session.query(Host).order_by(Host.host_name)
    for h in hosts:
        hosts_list.append(h.host_name)
    hosts_list_return = ",".join(hosts_list)
    return hosts_list_return

def add_hosts(host_id):
    try:
        hosts = Host(host_name=host_id)
        db.session.add(hosts)
        db.session.commit()
        return "done"
    except Exception as e:
        return "Error: ",e

def del_env(env_id):
    try:
        env = Env.query.filter_by(env_name=env_id).delete()
        db.session.commit()
        return "done"
    except Exception as e:
        return "Error: ",e

def del_host(host_id):
    try:
        host = Host.query.filter_by(host_name=host_id).delete()
        db.session.commit()
        return "done"
    except Exception as e:
        return "Error: ",e

def del_app(app_id):
    try:
        app = App.query.filter_by(app_name=app_id).delete()
        db.session.commit()
        return "done"
    except Exception as e:
        return "Error: ",e

def del_bu(bu_id):
    try:
        bu = Bu.query.filter_by(bu_name=bu_id).delete()
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
    db.session.flush()

    return "done"
