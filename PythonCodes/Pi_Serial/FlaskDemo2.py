# make a webpage - https://towardsdatascience.com/python-webserver-with-flask-and-raspberry-pi-398423cc6f5d

from flask import Flask

app = Flask(__name__)
@app.route('/')
def index():
    return 'Hello world'
if __name__ == '__main__':
    app.run(debug=True, port=80, host='192.168.86.128')