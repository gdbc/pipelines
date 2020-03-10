#!/usr/bin/python3.4
from flask import Flask, jsonify, request, Response
from random import randrange
from create_pv import cpv
from create_pvc import cpvc

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
def getpvs():
    token = request.args.get('token')
    if token in tokens:
        return 'getpvs'
    else:
        return '"message": {"auth": "failed"}'

@app.route('/getpvcs')
def getpvcs():
    token = request.args.get('token')
    if token in tokens:
        return 'getpvcs'
    else:
        return '"message": {"auth": "failed"}'

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
    except Exceptions as e:
        print("error: %s", e)
        return '"message": {"error": "Something borked!"}"'

@app.route('/createpvcs')
def createpvcs():
    try: 
        token      = request.args.get('token')
        namespace  = request.args.get('namespace')
        pvname     = request.args.get('pvname')
        volumename = request.args.get('volumename')
        print("token: ", token)
        print("namespace: ", namespace)
        print("pvname: ", pvname)
        print("volumename: ", volumename)
        if token in tokens:
            createpvc  = cpvc(namespace, pvname, volumename) 
            return createpvc
        else:
            return '"message": {"auth": "failed"}'
    except Exceptions as e:
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
