import json
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def root():
    if request.method == 'GET':
        return get()
    elif request.method == 'POST':
        return post()
    elif request.method == 'PUT':
        return put()
    else:
        return delete()

def get ():
    f = open('module-2-backend/week-1/data.json')
    data = json.load(f)
    return data

def post ():
    return 'POST'

def put ():
    return 'PUT'

def delete ():
    return 'DELETE'

if __name__ == '__main__':
    app.run(host='localhost',port=8000, debug=True)