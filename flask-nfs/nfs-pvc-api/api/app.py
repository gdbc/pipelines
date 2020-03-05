#!/usr/bin/python3.4
from flask import Flask, jsonify, request, Response
from random import randrange


app = Flask(__name__)


@app.route('/')
def get_randrange():
    one = request.args.get('one')
    two = request.args.get('two')
    #job = q.enqueue(randrange, start, stop, step, result_ttl=5000)
    return "hi"


if __name__ == '__main__':
    # Start server
    app.run(host='0.0.0.0', port=5000)
