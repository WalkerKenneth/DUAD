from flask import Flask

app = Flask(__name__)

@app.route('/')
def root():
    return "<h1>Hello, World!</h1>"

@app.route('/information')
def information():
    return {
        "year": 2024,
        "description": "Secondary Route",
    }

if __name__ == '__main__':
    app.run(host='localhost',port=8000, debug=True)