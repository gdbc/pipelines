#!/usr/bin/python3.4
from flask import Flask, jsonify, request, Response
from random import randrange
from create_pv import cpv
from create_pvc import cpvc
from delete_pv import dpv
from delete_pvc import dpvc
from get_pvcs import getpvcs
from get_pvs import getpvs
from check_pv_rbac import checkrbac

app = Flask(__name__)

tokens=['123asdffdaTGyI123zZ1']


@app.route('/')
def get_randrange():
    token = request.args.get('one')
    one   = request.args.get('one')
    two   = request.args.get('two')
    #job = q.enqueue(randrange, start, stop, step, result_ttl=5000)
    return "hi"

@app.route('/getpvs')
def gpvs():
    try:
        token = request.args.get('token')
        if token in tokens:
            gtpvs = getpvs()
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
        if token in tokens:
            gtpvcs = getpvcs(namespace)
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
        print("token: ", token)
        print("pvname: ", pvname)
        print("server: ", server)
        print("path: ", path)
        if token in tokens:
            createpv = cpv(pvname, server, path)
            return createpv
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
        print("token: ", token)
        print("namespace: ", namespace)
        print("pvname: ", pvname)
        print("pvcname: ", pvcname)
        if token in tokens:
            createpvc  = cpvc(namespace, pvcname, pvname) 
            return createpvc
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
        print("token: ", token)
        print("pvname: ", pvname)
        if token in tokens:
            deletepv = dpv(pvname)
            return deletepv
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
        print("token: ", token)
        print("pvcname: ", pvcname)
        print("namespace: ", namespace)
        if token in tokens:
            deletepvc = dpvc(namespace, pvcname)
            return deletepvc
        else:
            return '"message": {"auth": "failed"}'
    except Exception as e:
        print("error: %s", e)
        return '"message": {"error": "Something borked!"}"'


@app.route('/getauth')
def getauth():
    token = request.args.get('token')
    if token in tokens:
        return 'getauth'
    else:
        return '"message": {"auth": "failed"}'


if __name__ == '__main__':
    # Start server
    app.run(host='0.0.0.0', port=5000)
