# make a webpage - https://towardsdatascience.com/python-webserver-with-flask-and-raspberry-pi-398423cc6f5d
mkdir rpiWebServer
cd rpiWebServer
mkdir static
mkdir templates

python3
f = open('test.py','w')
f.write("from flask import Flask\n")
f.write("app = Flask(__name__)\n")
f.write("@app.route('/')\n")
f.write("def index():\n")
f.write("    return 'Hello world'\n")
f.write("if __name__ == '__main__':\n")
f.write("    app.run(debug=True, port=80,host='192.168.86.128')\n")
f.close()
exit()

sudo python3 test.py 
