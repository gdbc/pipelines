#!/usr/bin/python3.4
from flask import Flask, jsonify, request, Response
from random import randrange
from create_pv import cpv
from create_pvc import cpvc
from delete_pv import dpv
from delete_pvc import dpvc
from get_pvcs import getpvcs
from get_pvs import getpvs
from check_pv_rbac import checkpvrbac
from check_pv_rbac import getpv
from check_pv_rbac import getpvnfsinfo
from get_auths import getrbac
from get_tokens import hastoken


app = Flask(__name__)


@app.route('/')
def get_randrange():
    token = request.args.get('one')
    one   = request.args.get('one')
    two   = request.args.get('two')
    #job = q.enqueue(randrange, start, stop, step, result_ttl=5000)
    return "hi"

@app.route('/getauths')
def gassls():
    try:
        token = request.args.get('token')
        if hastoken(token):
            gta = getrbac(token)
            return gta
        else:
            return '"message": {"getauth": "dont seem to have any pvs authorized"}'
    except Exception as e:
        print("error: %s", e)
        return '"message": {"error": "Something borked in getauth"}"'


@app.route('/getpvs')
def gpvs():
    try:
        token = request.args.get('token')
        clstr = request.args.get('cluster')
        if hastoken(token):
            gtpvs = getpvs(clstr)
            return gtpvs
        else:
            return '"message": {"auth": "failed"}'
    except Exception as e:
        print("error: %s", e)
        return '"message": {"error": "Something borked in getpvs"}"'

@app.route('/getpvcs')
def gpvcs():
    try: 
        token     = request.args.get('token')
        namespace = request.args.get('namespace')
        clstr = request.args.get('cluster')
        if hastoken(token):
            gtpvcs = getpvcs(clstr, namespace)
            return gtpvcs
        else:
            return '"message": {"auth": "failed"}'
    except Exception as e:
        print("error: %s", e)
        return '"message": {"error": "Something borked in getpvs"}"'

@app.route('/createpvs')
def createpvs():
    try: 
        token    = request.args.get('token')
        pvname   = request.args.get('pvname')
        server   = request.args.get('nfsserver')
        path     = request.args.get('path')
        clstr    = request.args.get('cluster')
        print("token: ", token)
        print("pvname: ", pvname)
        print("server: ", server)
        print("path: ", path)
        if hastoken(token):
            if checkpvrbac(clstr, token, server, path):
                createpv = cpv(clstr, pvname, server, path)
                return createpv
            else:
                return '"message": {"auth": "failed"}'
        else:
            return '"message": {"auth": "failed"}'
    except Exception as e:
        print("error: %s", e)
        return '"message": {"error": "Something borked!"}"'

@app.route('/createpvcs')
def createpvcs():
    try: 
        token      = request.args.get('token')
        namespace  = request.args.get('namespace')
        pvname     = request.args.get('pvname')
        pvcname    = request.args.get('pvcname')
        clstr      = request.args.get('cluster')
        print("token: ", token)
        print("namespace: ", namespace)
        print("pvname: ", pvname)
        print("pvcname: ", pvcname)
        if hastoken(token):
            srv, path = getpvnfsinfo(clstr, token, pvname)
            if srv is not "none" and path is not "none":
                if checkpvrbac(clstr, token, srv, path):
                   createpvc  = cpvc(clstr, namespace, pvcname, pvname) 
                   return createpvc
                else:
                    return '"message": {"auth": "failed"}'
            else:
                return '"message": {"auth": "failed"}'
        else:
            return '"message": {"auth": "failed"}'
    except Exception as e:
        print("error: %s", e)
        return '"message": {"error": "Something borked!"}"'

@app.route('/deletepvs')
def deletepvs():
    try:
        token    = request.args.get('token')
        pvname   = request.args.get('pvname')
        clstr    = request.args.get('cluster')
        print("token: ", token)
        print("pvname: ", pvname)
        if hastoken(token):
            server, mount = getpvnfsinfo(clstr, token, pvname)
            getrbac = checkpvrbac(clstr, token, server, mount)
            if getrbac:
                deletepv = dpv(clstr, pvname)
                return deletepv
            else:
                return '"message": {"auth": "failed"}'
            return '"message": {"auth": "failed"}'
        else:
            return '"message": {"auth": "failed"}'
    except Exception as e:
        print("error: %s", e)
        return '"message": {"error": "Something borked!"}"'

@app.route('/deletepvcs')
def deletepvcs():
    try:
        token     = request.args.get('token')
        pvcname   = request.args.get('pvcname')
        namespace = request.args.get('namespace')
        clstr     = request.args.get('cluster')
        print("token: ", token)
        print("pvcname: ", pvcname)
        print("namespace: ", namespace)
        if hastoken(token):
            gpv = getpv(clstr, namespace, pvcname)
            srv, path = getpvnfsinfo(clstr, token, gpv)
            if srv is not "none" and path is not "none":
                if checkpvrbac(clstr, token, srv, path):
                    deletepvc = dpvc(clstr, namespace, pvcname)
                    return deletepvc
                else:
                   return '"message": {"auth": "failed"}'
            else:
                return '"message": {"auth": "failed"}'
        else:
            return '"message": {"auth": "failed"}'
    except Exception as e:
        print("error: %s", e)
        return '"message": {"error": "Something borked!"}"'


@app.route('/getauth')
def getauth():
    token = request.args.get('token')
    if hastoken(token):
        return 'getauth'
    else:
        return '"message": {"auth": "failed"}'


if __name__ == '__main__':
    # Start server
    app.run(host='0.0.0.0', port=5000)
