from flask import Flask
from flask import request
import os
import json

app = Flask(__name__)

@app.route("/")
def home():
    return "welcome"

@app.route("/shutdown")
def shutdown():
    func = request.environ.get('werkzeug.server.shutdown')
    print("server shutting down..")
    func()
    os._exit(0)

@app.route("/getTables")
def getTables():
    tablesFile = open("tables.json","r+")
    return str(json.load(tablesFile)).replace("\'","\"")

@app.route("/getMenu")
def getMenu():
    menuFile = open("menu.json","r+")
    return str(json.load(menuFile)).replace("\'","\"")

@app.route("/setMenu", methods=['POST'])
def setMenu():
    menuFile = open("menu.json","r+")
    data = request.get_json()
    menuFile.writelines(json.dumps(data));
    return json.dumps({
        "status":200,
        "body":"success"
    })

@app.route("/setTables", methods=['POST'])
def setTables():
    tablesFile = open("tables.json","r+")
    data = request.get_json()
    tablesFile.writelines(json.dumps(data));
    return json.dumps({
        "status":200,
        "body":"success"
    })

if __name__ == "__main__":

    app.run(host='192.168.16.9')