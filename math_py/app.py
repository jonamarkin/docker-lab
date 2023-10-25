from flask import Flask, render_template, request, make_response, jsonify
import requests

app = Flask(__name__, instance_relative_config=True)

@app.route('/add')
def add():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    if a and b:
        return make_response(jsonify(s=a+b), 200) # HTTP 200 OK
    else:
        return make_response('Invalid input\n', 400) # HTTP 400 BAD REQUEST

#add other routes here

#Subtraction route
@app.route('/sub')
def subtract():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    if a and b:
        return make_response(jsonify(s=a-b), 200)
    else:
        return make_response('Invalid input\n', 400)
    
#Multiplication route
@app.route('/mul')
def multiply():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    if a and b:
        return make_response(jsonify(s=a*b), 200)
    else:
        return make_response('Invalid input\n', 400)
    
#Division route
@app.route('/div')
def divide():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    if a and b:
        return make_response(jsonify(s=a/b), 200)
    else:
        return make_response('Invalid input\n', 400)
    
#Modulo route
@app.route('/mod')
def modulo():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    if a and b:
        return make_response(jsonify(s=a%b), 200)
    else:
        return make_response('Invalid input\n', 400)

def create_app():
    return app